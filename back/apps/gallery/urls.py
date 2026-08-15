from django.urls import path
from .views import (galleries_list,gallery_detail,upload_media,photos_list,photo_delete)

urlpatterns = [
    path("", galleries_list, name="galleries-list"),
    path("<int:id>/", gallery_detail, name="gallery-detail"),
    path("photos/<int:id>/upload/", upload_media, name="gallery-upload"),
    path("photos/", photos_list, name="photo-detail"),
    path("photos/<int:id>/delete/", photo_delete, name="photo_delete")

]