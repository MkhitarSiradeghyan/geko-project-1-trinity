from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Gallery, MediaItem
from .serializers import GallerySerializer, MediaItemSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def gallery_list(request):
    
    if request.method == "GET":
        galleries = Gallery.objects.filter(is_public=True) | Gallery.objects.filter(owner=request.user)
        serializer = GallerySerializer(galleries.distinct(),many=True,context={"request": request})
        return Response(serializer.data)

    if request.method == "POST":
        serializer = GallerySerializer(data=request.data,context={"request": request})

        if serializer.is_valid():
            serializer.save(owner=request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)