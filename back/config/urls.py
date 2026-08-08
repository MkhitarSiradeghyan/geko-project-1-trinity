from django.contrib import admin
from django.urls import path, include
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/contacts/", include("apps.contacts.urls")),
    path("api/tours/",include("apps.tours.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/", include("apps.users.urls")),
]
