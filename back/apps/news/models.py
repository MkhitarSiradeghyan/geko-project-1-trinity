from django.conf import settings
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

        def __str__(self):
            return self.name

class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        ARCHIVED = "ARCHIVED", "Archived"

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    summary = models.TextField(max_length=500, blank=True)
    cover_image = models.ImageField(
        upload_to="news/covers/%Y/%m/", null=True, blank=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

class Meta:
    ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title