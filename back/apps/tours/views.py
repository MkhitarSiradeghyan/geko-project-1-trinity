from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tour
from .serializers import TourSerializer


@api_view(["GET", "POST"])
def tours_list(request):
    if request.method == "GET":
        tours = Tour.objects.all()
        serializer = TourSerializer(tours,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def tour_detail(request, id):

    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:

        return Response({"error": "Tour not found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TourSerializer(tour)

        return Response(serializer.data,status=status.HTTP_200_OK)


    elif request.method == "PUT":
        serializer = TourSerializer(tour,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        tour.delete()
        return Response({"message": "Tour deleted successfully"},status=status.HTTP_204_NO_CONTENT)