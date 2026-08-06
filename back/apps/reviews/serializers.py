from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "tour",
            "rating",
            "comment",
            "created_at"
        ]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )
        return value

    def validate(self, data):
        request = self.context.get("request")

        if request and request.method == "POST":
            if Review.objects.filter(
                user=request.user,
                tour=data.get("tour")
            ).exists():
                raise serializers.ValidationError(
                    "You have already reviewed this tour."
                )

        return data