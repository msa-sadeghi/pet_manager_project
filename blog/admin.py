from django.contrib import admin
from .models import Post, Tag, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title", "content")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
