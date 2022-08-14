from django_filters import CharFilter, FilterSet, NumberFilter

from reviews.models import Titles


class TitleFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')
    year = NumberFilter(field_name='year')

    class Meta:
        model = Titles
        fields = ('genre', 'category', 'name', 'year',)
