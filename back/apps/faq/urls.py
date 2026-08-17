from django.urls import path
from . import views


urlpatterns = [
    path("", views.faq_list_create),
    path("<int:pk>/", views.faq_detail),
]