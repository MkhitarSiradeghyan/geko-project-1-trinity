from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.name

class Article(models.Model):

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
        (ARCHIVED, "Archived"),
    ]

    title = models.CharField(
        max_length=255
    )


    slug = models.SlugField(
        unique=True
    )

    content = models.TextField()

    summary = models.TextField(
        max_length=500,
        blank=True
    )

    cover_image = models.ImageField(
        upload_to="news/covers/%Y/%m/",
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        related_name="articles",
        on_delete=models.CASCADE
    )

    status = models.CharField (
        max_length=20,
        choices=STATUS_CHOICES,
        default=DRAFT
    )

    published_at = models.DateTimeField (
        null=True,
        blank=True
    )

    created_at = models.DateTimeField (
        auto_now_add=True
    )

    updated_at = models.DateTimeField (
        auto_now = True
    )

    def __str__(self):
        return self.title