from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from api.permissions import (IsAdminOrReadOnly)


class CreateListDestroytViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
