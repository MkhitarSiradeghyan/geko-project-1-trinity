from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    register,
    logout,
    me,
    CustomTokenObtainPairView,
)


urlpatterns = [

    path(
        "auth/register/",
        register,
        name="register"
    ),

    path(
        "auth/login/",
        CustomTokenObtainPairView.as_view(),
        name="login"
    ),

    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    path(
        "auth/logout/",
        logout,
        name="logout"
    ),

    path(
        "users/me/",
        me,
        name="me"
    ),
]