from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from spares_tracker.users.models import BaseUser
from spares_tracker.users.services import user_create


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'is_superuser', 'is_active', 'created_at', 'updated_at')

    search_fields = ('email',)

    list_filter = ('is_active', 'is_admin', 'is_superuser')

    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (
            None, {
                'fields': ('email',)
            }
        ),
        (
            "Booleans", {
                "fields": ("is_active", "is_admin", "is_superuser")
            }
        ),
        (
            "Groups and Permissions", {
                "fields": ('groups', 'user_permissions',)
            }
        ),
        (
            "Timestamps", {
                "fields": ("created_at", "updated_at")
            }
        )
    )

    readonly_fields = ("created_at", "updated_at", )

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            user_info = form.cleaned_data
            del user_info['groups']
            del user_info['user_permissions']
            del user_info['is_superuser']
            user_create(**user_info)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
