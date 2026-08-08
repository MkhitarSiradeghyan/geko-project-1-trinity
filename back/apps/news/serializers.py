from rest_framework import serializers
from .models import Category, Article

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "slug",
            "summary",
            "cover_image",
            "published_at",
            "category",
        ]

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "summary",
            "cover_image",
            "published_at",
            "category",
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
