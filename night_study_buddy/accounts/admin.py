from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Information', {
            'fields': ('role', 'phone', 'class_name', 'parent_email')
        }),
    )

    list_display = (
        'username',
        'email',
        'role',
        'phone',
        'class_name',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_active',
    )


admin.site.register(User, CustomUserAdmin)