
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("news/", include("apps.news.urls")),
=======
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/tours/",include("apps.tours.urls")),

>>>>>>> dev
]
