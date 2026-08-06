from rest_framework import serializers
from .models import ContactSubmission


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "name", "email", "phone", "message", "created_at"]

    def validate(self, data):
        email = data.get("email")
        phone = data.get("phone")
        if not email and not phone:
            raise serializers.ValidationError(
                "You must provide at least an email or a phone number."
            )
        return data