from django.db import models
from django.contrib.auth.models import User


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="galleries")
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MediaItem(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.CASCADE,related_name="photos")
    image = models.ImageField(upload_to="galleries/%Y/%m/")
    caption = models.CharField(max_length=255,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
