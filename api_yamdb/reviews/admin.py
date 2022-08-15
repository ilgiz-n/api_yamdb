from django.contrib import admin

from reviews.models import Categories, Genres, Title


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
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
    )
    list_editable = (
        'description',
        'category',
        'rating',
    )
    search_fields = ('name', 'year', 'rating')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Genres, CategoriesAdmin)
admin.site.register(Title, TitlesAdmin)
