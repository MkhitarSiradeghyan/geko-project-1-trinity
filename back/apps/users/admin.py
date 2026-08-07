from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "role",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Role information",
            {
                "fields": (
                    "role",
                    "created_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
    )


    def has_module_permission(self, request):

        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


    def has_view_permission(self, request, obj=None):

        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


    def has_change_permission(self, request, obj=None):

        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


    def has_delete_permission(self, request, obj=None):

        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )