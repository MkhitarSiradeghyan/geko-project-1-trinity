from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists"
            )

        return value

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role="USER"
        )

        return user



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "role",
            "created_at",
        )



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token["username"] = user.username
        token["role"] = user.role

        return token


    def validate(self, attrs):

        data = super().validate(attrs)

        data["username"] = self.user.username
        data["role"] = self.user.role

        return data