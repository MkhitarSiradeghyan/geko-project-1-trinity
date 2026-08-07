from django.db.models import Avg, Count

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

from rest_framework.response import Response
from rest_framework import status


from .models import Review
from .serializers import ReviewSerializer



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_list_create(request):


    if request.method == "GET":

        reviews = Review.objects.all()


        tour = request.GET.get("tour")
        rating = request.GET.get("rating")


        if tour:
            reviews = reviews.filter(
                tour=tour
            )


        if rating:
            reviews = reviews.filter(
                rating=rating
            )


        serializer = ReviewSerializer(
            reviews,
            many=True
        )


        return Response(
            serializer.data
        )



    serializer = ReviewSerializer(
        data=request.data,
        context={
            "request": request
        }
    )


    if serializer.is_valid():

        serializer.save(
            user=request.user
        )


        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )




@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_detail(request, pk):


    try:

        review = Review.objects.get(
            id=pk
        )


    except Review.DoesNotExist:

        return Response(
            status=status.HTTP_404_NOT_FOUND
        )



    if request.method == "GET":

        serializer = ReviewSerializer(
            review
        )

        return Response(
            serializer.data
        )



    if review.user != request.user:

        return Response(
            {
                "error":
                "You can edit only your review"
            },
            status=status.HTTP_403_FORBIDDEN
        )



    if request.method == "PUT":

        serializer = ReviewSerializer(
            review,
            data=request.data,
            partial=True,
            context={
                "request": request
            }
        )


        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



    review.delete()


    return Response(
        status=status.HTTP_204_NO_CONTENT
    )





@api_view(["GET"])
def review_statistics(request):

    tour = request.GET.get("tour")


    reviews = Review.objects.filter(
        tour=tour
    )


    average = reviews.aggregate(
        avg=Avg("rating")
    )


    breakdown = reviews.values(
        "rating"
    ).annotate(
        count=Count("id")
    )


    return Response(
        {
            "average_rating": average["avg"],
            "breakdown": breakdown
        }
    )