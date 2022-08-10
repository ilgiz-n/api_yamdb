from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from reviews.models import Reviews, Comments, Titles
from .serializers import ReviewsSerializer, CommentsSerializer
from .permissions import AdminModeratorAuthorPermission


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = [AdminModeratorAuthorPermission]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        new_queryset = Reviews.objects.filter(title=title_id)
        return new_queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        titles = get_object_or_404(Titles, id=title_id)
        serializer.save(author=self.request.user,
                        titles=titles)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [AdminModeratorAuthorPermission]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        new_queryset = Comments.objects.filter(review=review_id)
        return new_queryset

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Reviews, id=review_id)
        serializer.save(author=self.request.user,
                        review=review)
