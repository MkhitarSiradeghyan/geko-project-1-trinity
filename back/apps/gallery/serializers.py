from rest_framework import serializers
from .models import Gallery, MediaItem


class MediaItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = MediaItem
        fields = [
            "id",
            "gallery",
            "image",
            "image_url",
            "caption",
            "uploaded_at",
        ]

        read_only_fields = [
            "id",
            "uploaded_at",
            "image_url",
        ]

    def validate_image(self, image):
        allowed_types = [
            "image/jpeg",
            "image/png",
            "image/webp",
        ]

        if image.content_type not in allowed_types:
            raise serializers.ValidationError("Only JPEG, PNG and WebP images are allowed.")
        return image

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)

        return obj.image.url if obj.image else None


    
class GallerySerializer(serializers.ModelSerializer):
    
    photos = MediaItemSerializer(many=True,read_only=True)
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "description",
            "owner",
            "is_public",
            "photos",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "owner",
            "photos",
            "created_at",
            "updated_at",
        ]