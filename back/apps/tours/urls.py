from django.urls import path
from .views import tours_list,tour_detail,tour_image_create,tour_image_delete,images_list


urlpatterns = [
    path("", tours_list, name="tours-list"),
    path("<int:id>/", tour_detail, name="tour-detail"),
    path("images/<int:id>/create/",tour_image_create,name="tour-image-create"),
    path("images/",images_list,name="images_list"),
    path("images/<int:id>/delete/",tour_image_delete,name="tour-image-delete"),
    
]