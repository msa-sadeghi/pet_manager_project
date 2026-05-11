from django.contrib import admin
from django.utils.html import format_html
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "name",
        "species",
        "gender",
        "birth_date",
        "get_age_display",
        "color",
        "is_neutered",
        "created_at",
        "photo_preview",
    )
    search_fields = (
        "owner__user__username",
        "name",
        "species",
        "breed",
        "microchip_id",
    )
    list_filter = (
        "species",
        "gender",
        "is_neutered",
        "created_at",
        "owner__city",
    )
    ordering = ("owner__user__last_name", "name")
    readonly_fields = ("created_at", "updated_at", "get_age_display")

    def owner_display(self, obj):
        return str(obj.owner)

    owner_display.short_description = "صاحب"

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src={} style="">', obj.photo.url)
        return "عکس"

    photo_preview.short_description = "عکس"
