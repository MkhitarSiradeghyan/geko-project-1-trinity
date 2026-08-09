from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tour
from .serializers import TourSerializer
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)


@extend_schema(
    summary="Get tours list or create a tour",
    description="Returns all available tours or creates a new tour.",
    request=TourSerializer,
    responses={
        200: TourSerializer(many=True),
        201: TourSerializer,
        400: OpenApiResponse(
            description="Invalid request data"
        ),
    },
    examples=[
        OpenApiExample(
            "Tour example",
            value={
                "title": "Armenia Tour",
                "price": 150000,
            },
            request_only=True,
        ),
    ],
)
@api_view(["GET", "POST"])
def tours_list(request):

    if request.method == "GET":
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    elif request.method == "POST":
        serializer = TourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@extend_schema(
    summary="Get, update or delete a tour",
    description="Retrieves, updates or deletes a specific tour.",
    request=TourSerializer,
    responses={
        200: TourSerializer,
        204: OpenApiResponse(
            description="Tour deleted successfully"
        ),
        400: OpenApiResponse(
            description="Invalid request data"
        ),
        404: OpenApiResponse(
            description="Tour not found"
        ),
    },
)
@api_view(["GET", "PUT", "DELETE"])
def tour_detail(request, id):

    try:
        tour = Tour.objects.get(id=id)

    except Tour.DoesNotExist:
        return Response(
            {"error": "Tour not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = TourSerializer(tour)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    elif request.method == "PUT":
        serializer = TourSerializer(
            tour,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        tour.delete()

        return Response(
            {"message": "Tour deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )