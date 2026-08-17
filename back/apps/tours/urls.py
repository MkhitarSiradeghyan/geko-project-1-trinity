from django.urls import path
from .views import tours_list,tour_create, tour_detail,tour_delete,tour_image_create,tour_image_delete


urlpatterns = [
    path("", tours_list, name="tours-list"),
    path("create/", tour_create, name="tour-create"),
    path("detail/<int:id>/", tour_detail, name="tour-detail"),
    path("delete/<int:id>/", tour_delete, name="tour-detail"),
    path("images/<int:id>/create/",tour_image_create,name="tour-image-create"),
    path("images/<int:id>/delete/",tour_image_delete,name="tour-image-delete"),
    
]