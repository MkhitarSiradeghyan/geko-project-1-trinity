from django.urls import path

from .views import category_list, category_detail, article_list, article_detail

urlpatterns = [
    path(
        "categories/",
        category_list,
        name="category-list",
    ),
    path(
        "categories/<slug:slug>/",
        category_detail,
        name="category-detail",
    ),

    path(
        "articles/",
        article_list,
        name="article-list",
    ),
    path(
        "articles/<slug:slug>/",
        article_detail,
        name="article-detail",
    ),
]