from django.contrib import admin
from .models import Tag, Category, CategoryDetail, Article, ArticleDetail

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(CategoryDetail)
admin.site.register(Article)
admin.site.register(ArticleDetail)