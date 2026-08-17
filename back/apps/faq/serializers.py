from rest_framework import serializers

from .models import FaqEntry


class FaqEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqEntry
        fields = [
            "id",
            "question",
            "answer",
        ]
        read_only_fields = [
            "id",
        ]