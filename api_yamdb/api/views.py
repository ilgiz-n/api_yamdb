from rest_framework import filters, viewsets
from reviews.models import Categories, Genres, Titles
from .permissions import (AdminModeratorAuthorPermission,
                          AdminSuperuserPermission)
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitlesSerializer)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (AdminModeratorAuthorPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (AdminModeratorAuthorPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (AdminModeratorAuthorPermission,)
    filter_backends = (filters.DjangoFilterBackend,)

