from django.contrib import admin
from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "slug"
    )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "status",
        "created_at"
    )

    list_filter = (
        "status",
        "category"
    )

    search_fields = (
        "title",
        "content"
    )