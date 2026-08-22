from django.urls import path
from .views import AboutDetailView

urlpatterns = [
    path('about/', AboutDetailView.as_view(), name='about-detail'),
]