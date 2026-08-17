from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import FaqEntry
from .permissions import IsStaffOrReadOnly
from .serializers import FaqEntrySerializer


@extend_schema(
    methods=["GET"],
    responses={200: FaqEntrySerializer(many=True)},
)
@extend_schema(
    methods=["POST"],
    request=FaqEntrySerializer,
    responses={201: FaqEntrySerializer},
)
@api_view(["GET", "POST"])
@permission_classes([IsStaffOrReadOnly])
def faq_list_create(request):

    if request.method == "GET":

        faqs = FaqEntry.objects.all()

        if not (
            request.user.is_authenticated
            and request.user.is_staff
        ):
            faqs = faqs.filter(
                is_active=True
            )

        serializer = FaqEntrySerializer(
            faqs,
            many=True
        )

        return Response(
            serializer.data
        )

    serializer = FaqEntrySerializer(
        data=request.data
    )

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
    methods=["GET"],
    responses={200: FaqEntrySerializer},
)
@extend_schema(
    methods=["PUT"],
    request=FaqEntrySerializer,
    responses={200: FaqEntrySerializer},
)
@extend_schema(
    methods=["DELETE"],
    responses={204: None},
)
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsStaffOrReadOnly])
def faq_detail(request, pk):

    try:

        faq = FaqEntry.objects.get(
            id=pk
        )

    except FaqEntry.DoesNotExist:

        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        if (
            not faq.is_active
            and not (
                request.user.is_authenticated
                and request.user.is_staff
            )
        ):
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FaqEntrySerializer(
            faq
        )

        return Response(
            serializer.data
        )

    if request.method == "PUT":

        serializer = FaqEntrySerializer(
            faq,
            data=request.data,
            partial=True
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

    faq.delete()

    return Response(
        status=status.HTTP_204_NO_CONTENT
    )