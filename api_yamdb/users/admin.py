from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class UserAdmin(UserAdmin):
    model = User
    list_display = (
        'username',
        'email',
        'role',
        'first_name',
        'last_name',
    )
    fieldsets = (
        (('User'), {'fields': list_display}),
    )
    search_fields = ('username', 'role',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
