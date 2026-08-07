from django.urls import path
from . import views

urlpatterns = [
    path("tours/",views.tours_list,name="tours-list"),
    path("tours/<int:id>/",views.tour_detail,name="tour-detail"),

              ]