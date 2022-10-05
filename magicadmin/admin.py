from django.contrib import admin
from .models import MagicLink


class MagicLinkAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "expires_at",
        "user",
        "already_used",
    )
    readonly_fields = [
        "created_at",
        "used_at",
        "already_used",
        "user",
        "secret_identifier"
    ]

admin.site.register(MagicLink, MagicLinkAdmin)