from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model

from .models import CustomUser
from .serializers import (
    UserRegisterSerializer,
    CustomTokenObtainPairSerializer,
)

from .permissions import (
    IsAdmin,
    IsOwnerOrAdmin,
)


User = get_user_model()



class UserModelTests(APITestCase):


    def test_user_created_with_default_role(self):

        user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="password123"
        )


        self.assertEqual(
            user.role,
            CustomUser.Roles.USER
        )



    def test_admin_property(self):

        user = User.objects.create_user(
            username="normal",
            password="password123"
        )


        admin = User.objects.create_user(
            username="admin",
            password="password123",
            role="ADMIN"
        )


        self.assertFalse(
            user.is_admin
        )


        self.assertTrue(
            admin.is_admin
        )





class SerializerTests(APITestCase):


    def test_register_serializer_valid(self):

        data = {
            "username":"newuser",
            "email":"new@test.com",
            "password":"StrongPassword123!"
        }


        serializer = UserRegisterSerializer(
            data=data
        )


        self.assertTrue(
            serializer.is_valid()
        )



    def test_duplicate_email_rejected(self):

        User.objects.create_user(
            username="user1",
            email="same@test.com",
            password="password123"
        )


        data = {
            "username":"user2",
            "email":"same@test.com",
            "password":"StrongPassword123!"
        }


        serializer = UserRegisterSerializer(
            data=data
        )


        self.assertFalse(
            serializer.is_valid()
        )



    def test_token_contains_role(self):

        user = User.objects.create_user(
            username="tokenuser",
            password="password123"
        )


        token = CustomTokenObtainPairSerializer.get_token(
            user
        )


        self.assertEqual(
            token["role"],
            "USER"
        )





class PermissionTests(APITestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            username="user",
            password="password123"
        )


        self.admin = User.objects.create_user(
            username="admin",
            password="password123",
            role="ADMIN"
        )


    def test_admin_permission(self):

        permission = IsAdmin()


        request = type(
            "Request",
            (),
            {
                "user": self.admin
            }
        )


        self.assertTrue(
            permission.has_permission(
                request,
                None
            )
        )



        request.user = self.user


        self.assertFalse(
            permission.has_permission(
                request,
                None
            )
        )




    def test_owner_permission(self):

        permission = IsOwnerOrAdmin()


        request = type(
            "Request",
            (),
            {
                "user": self.user
            }
        )


        self.assertTrue(
            permission.has_object_permission(
                request,
                None,
                self.user
            )
        )


        self.assertFalse(
            permission.has_object_permission(
                request,
                None,
                self.admin
            )
        )



        request.user = self.admin


        self.assertTrue(
            permission.has_object_permission(
                request,
                None,
                self.user
            )
        )





class AuthenticationAPITests(APITestCase):


    def test_register_api(self):

        url = "/api/auth/register/"


        response = self.client.post(
            url,
            {
                "username":"apiuser",
                "email":"api@test.com",
                "password":"StrongPassword123!"
            }
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )



    def test_login_api(self):

        User.objects.create_user(
            username="loginuser",
            password="password123"
        )


        response = self.client.post(
            "/api/auth/login/",
            {
                "username":"loginuser",
                "password":"password123"
            }
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


        self.assertIn(
            "access",
            response.data
        )



    def test_me_requires_authentication(self):

        response = self.client.get(
            "/api/users/me/"
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )