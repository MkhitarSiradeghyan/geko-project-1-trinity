from rest_framework import serializers
from .models import Gallery, MediaItem


MAX_FILE_SIZE = 5*1024*1024

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp",
}

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
            "file_size",
            "uploaded_at",
        ]

        read_only_fields = [
            "file_size",
            "uploaded_at",
            "image_url",
        ]

    def validate_image(self, image):
        if image.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("Image size must not exceed 5 MB.")
        extension = image.name.split(".")[-1].lower()
        if extension not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError("Only JPEG, PNG and WebP images are allowed.")
        return image

    def create(self, validated_data):
        image = validated_data["image"]
        validated_data["file_size"] = image.size
        return super().create(validated_data)

    def get_image_url(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return None

        url = obj.image.url
        if request:
         return request.build_absolute_uri(url)
        return url


    
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