from django.urls import path
from . import views

urlpatterns = [
    path("", views.tours_list, name="tours-list"),
    path("<int:id>/", views.tour_detail, name="tour-detail"),
]
