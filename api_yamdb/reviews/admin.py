from django.contrib import admin

from .models import Categories, Genres, Titles


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class TitlesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
        'rating',
        'description',
        'category',
        'genre',
    )
    list_editable = (
        'description',
        'category',
        'rating',
        )
    search_fields = ('name', 'year', 'rating')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Titles)
