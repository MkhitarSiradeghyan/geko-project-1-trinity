from django.urls import path
from . import views



urlpatterns = [

    path(
        "",
        views.review_list_create
    ),


    path(
        "<int:pk>/",
        views.review_detail
    ),


    path(
        "statistics/",
        views.review_statistics
    ),

]