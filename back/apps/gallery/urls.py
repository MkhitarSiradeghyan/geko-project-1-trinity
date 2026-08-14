from django.urls import path

from .views import (
    gallery_list,
)


urlpatterns = [
    path(
        "galleries/",
        gallery_list,
        name="gallery-list",
    ),
]