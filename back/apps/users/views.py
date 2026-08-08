from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserRegisterSerializer,
    UserSerializer,
    CustomTokenObtainPairSerializer,
)


User = get_user_model()


# ---------------------------
# LOGIN
# ---------------------------

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



# ---------------------------
# REGISTER
# POST /api/auth/register/
# ---------------------------

@api_view(["POST"])
def register(request):

    serializer = UserRegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )



# ---------------------------
# ME
# GET /api/users/me/
# PUT /api/users/me/
# ---------------------------

@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def me(request):

    user = request.user

    if request.method == "GET":

        serializer = UserSerializer(user)

        return Response(serializer.data)


    elif request.method == "PUT":

        serializer = UserSerializer(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



# ---------------------------
# LOGOUT
# POST /api/auth/logout/
# ---------------------------

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):

    try:

        refresh_token = request.data["refresh"]

        token = RefreshToken(refresh_token)

        token.blacklist()

        return Response(
            {
                "message": "Logout successful"
            },
            status=status.HTTP_204_NO_CONTENT
        )

    except Exception:

        return Response(
            {
                "error": "Invalid refresh token"
            },
            status=status.HTTP_400_BAD_REQUEST
        )