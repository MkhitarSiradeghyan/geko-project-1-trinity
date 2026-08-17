from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tour,TourImage
from .serializers import TourSerializer,TourImageSerializer


@api_view(["GET"])
def tours_list(request):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["POST"])
def tour_create(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def tour_detail(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return Response({"message": "Tour not found."},status=status.HTTP_404_NOT_FOUND)
    serializer = TourSerializer(tour)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["PUT"])
def tour_update(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return Response({"message": "Tour not found."},status=status.HTTP_404_NOT_FOUND)

    serializer = TourSerializer(tour,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def tour_delete(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return Response({"message": "Tour not found."},status=status.HTTP_404_NOT_FOUND)
    
    tour.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Upload image

@api_view(["POST"])
def tour_image_create(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return Response({"message": "Tour not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = TourImageSerializer(data=request.data)

    if serializer.is_valid():
        is_main = serializer.validated_data.get("is_main",False)
        if is_main:
            tour.images.update(is_main=False)
        serializer.save(tour=tour)

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#Delete image

@api_view(["DELETE"])
def tour_image_delete(request, id):
    try:
        image = TourImage.objects.get(id=id)
    except TourImage.DoesNotExist:
        return Response({"message": "Image not found."},status=status.HTTP_404_NOT_FOUND)
    
    image.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)