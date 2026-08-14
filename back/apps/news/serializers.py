from rest_framework import serializers
from models import Category, CategoryDetails, Article, ArticleDetails

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDetails
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


class ArticleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetails
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    details = ArticleDetailsSerializer(read_only=True)

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