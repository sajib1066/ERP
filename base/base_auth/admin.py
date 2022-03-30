from django.contrib import admin

from base.base_auth import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'email', 'name', 'is_staff', 'is_active', 'date_joined',
        'last_updated'
    ]
    list_display_links = ['id', 'email', 'name']
    search_fields = ['email', 'name']
