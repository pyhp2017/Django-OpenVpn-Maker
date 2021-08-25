from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from Authentications.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'username', 'password', 'first_name', 'last_name', 'config'
        )}),
    )
