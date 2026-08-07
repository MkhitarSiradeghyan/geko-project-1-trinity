from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer


@api_view(["GET"])
def article_list(request):
    articles = (
        Article.objects.filter(status=Article.PUBLISHED)
        .select_related("author", "category")
        .order_by("-published_at")
    )
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def article_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "category"),
        slug=slug,
        status=Article.PUBLISHED,
    )
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data)