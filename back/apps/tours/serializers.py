from rest_framework import serializers
from .models import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            "id",
            "title",
            "price",
            "created_at"
        ]

    def validate(self, data):
        title = data.get("title")
        price = data.get("price")

        if title is not None:
            if title.strip() == "":
                raise serializers.ValidationError({"title": "Title cannot be empty."} )
        return data