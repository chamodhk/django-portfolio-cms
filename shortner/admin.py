from django.contrib import admin

# Register your models here.
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "title",
        "destination_url",
        "is_active",
        "click_count",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("code", "title", "destination_url")
    readonly_fields = ("click_count", "created_at", "updated_at")
    prepopulated_fields = {"code": ("title",)}