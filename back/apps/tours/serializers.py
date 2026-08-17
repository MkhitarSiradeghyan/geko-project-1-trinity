from rest_framework import serializers
from datetime import date
from .models import Tour,TourImage

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = [
            "id",
            "image",
            "is_main",
        ]

class TourSerializer(serializers.ModelSerializer):

    images = TourImageSerializer(many=True,read_only=True)

    class Meta:
        model = Tour
        fields = [
            "id",
            "title",
            "start_date",
            "end_date",
            "meal_plan",
            "transfer_type",
            "hotel_name",
            "hotel_type",
            "ticket_included",
            "baggage_included",
            "latitude",
            "longitude",
            "adults",
            "children_under_2",
            "children_2_12",
            "children_12_plus",
            "price",
            "currency",
            "airline_name",
            "images",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
     if not value.strip():
        raise serializers.ValidationError("Title cannot be empty or contain only whitespace.")
     return value

    def validate_price(self, value):
     if value <= 0:
        raise serializers.ValidationError("Price must be greater than 0.")
     return value

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")
        today = date.today()

        # Start date must be after today
        if start_date and start_date <= today:
            raise serializers.ValidationError({"start_date": "Start date must be in the future."})

        # End date must be after today
        if end_date and end_date <= today:
            raise serializers.ValidationError({"end_date": "End date must be in the future."})

        # End date must be after start date
        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError({"end_date": "End date must be after start date."})

        return attrs


