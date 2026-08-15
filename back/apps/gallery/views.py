from rest_framework import status
from rest_framework.decorators import (api_view,parser_classes,permission_classes,)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Gallery, MediaItem
from .serializers import GallerySerializer, MediaItemSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def galleries_list(request):

    if request.method == "GET":
        public_galleries = Gallery.objects.filter(is_public=True)
        my_galleries = Gallery.objects.filter(owner=request.user)
        galleries = list(public_galleries)

        for gallery in my_galleries:
            if gallery not in galleries:
                galleries.append(gallery)

        serializer = GallerySerializer(galleries,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def gallery_detail(request,id):
    try:
        gallery = Gallery.objects.get(id=id)
    except Gallery.DoesNotExist:
        return Response({"message": "Gallery not found."},status=status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == "GET":
        if (not gallery.is_public and gallery.owner != request.user and not request.user.is_staff):
            return Response({"message": "You do not have permission to view this gallery."},
                status=status.HTTP_403_FORBIDDEN)

        serializer = GallerySerializer(gallery)
        return Response(serializer.data)


    #PUT
    if (gallery.owner != request.user and not request.user.is_staff):
        return Response({"message": "You do not have permission to modify this gallery."},status=status.HTTP_403_FORBIDDEN)
    if request.method==["PUT"]:
        serializer = GallerySerializer( gallery,data=request.data,partial=request.method == "PUT")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    gallery.delete()
    return Response({"message": "Gallery deleted successfully."},status=status.HTTP_204_NO_CONTENT)

#Upload image

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def upload_media(request,id):
    try:
        gallery = Gallery.objects.get(id=id)
    except Gallery.DoesNotExist:
        return Response({"message": "Gallery not found."},status=status.HTTP_404_NOT_FOUND)

    if (gallery.owner != request.user and not request.user.is_staff):
        return Response({"message": "You do not have permission to upload to this gallery."},status=status.HTTP_403_FORBIDDEN)
    
    serializer = MediaItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(gallery=gallery)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#Photos list

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def photos_list(request):
    public_photos = MediaItem.objects.filter(gallery__is_public=True)
    my_photos = MediaItem.objects.filter(gallery__owner=request.user)
    photos = list(public_photos)

    for photo in my_photos:
        if photo not in photos:
            photos.append(photo)

    serializer = MediaItemSerializer(photos,many=True)
    return Response(serializer.data)


#Delete photo

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def photo_delete(request,id):

    try:
        photo = MediaItem.objects.get(id=id)
    except MediaItem.DoesNotExist:
        return Response(
            {"message": "Photo not found."},status=status.HTTP_404_NOT_FOUND)
    if (photo.gallery.owner != request.user and not request.user.is_staff):
        return Response({"message": "You do not have permission to delete this photo."},
                        status=status.HTTP_403_FORBIDDEN)
    photo.delete()
    return Response({"message": "Photo deleted successfully."},status=status.HTTP_204_NO_CONTENT)

