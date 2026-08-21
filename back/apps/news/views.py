from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, CategoryDetail, Article, ArticleDetail
from .serializers import CategorySerializer, CategoryDetailSerializer, ArticleSerializer, ArticleDetailSerializer


@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, slug ):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return Response(
            {"detail": "Category not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=request.method == "PATCH",
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    category.delete()

    return Response(
        status=status.HTTP_204_NO_CONTENT,
    )


@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def article_detail(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(
            {"detail": "Article not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        serializer = ArticleSerializer(
            article,
            data=request.data,
            partial=request.method == "PATCH",
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    article.delete()

    return Response(
        status=status.HTTP_204_NO_CONTENT,
    )