from rest_framework import serializers
from .models import Category, CategoryDetail, Article, ArticleDetail

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDetail
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    details = CategoryDetailSerializer(read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image",
            "is_active",
            "details",
            "created_at",
            "updated_at",
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    details = ArticleDetailSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "category",
            "title",
            "slug",
            "short_description",
            "content",
            "cover_image",
            "is_published",
            "details",
            "created_at",
            "updated_at",
        ]