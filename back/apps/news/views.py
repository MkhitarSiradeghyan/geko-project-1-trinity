from django.views.generic import ListView, DetailView
from .models import Article, Category


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"

    def get_queryset(self):
        return (
            Article.objects.filter(status=Article.PUBLISHED)
            .select_related("author", "category")
            .order_by("-published_at")
        )


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Article.objects.filter(
            status=Article.PUBLISHED
        ).select_related("author", "category")


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"