from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer


@api_view(["GET", "POST"])
def contact_list(request):
    if request.method == "POST":
        serializer = ContactSubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # GET -> admin only
    if not IsAdminUser().has_permission(request, None):
        return Response(status=status.HTTP_403_FORBIDDEN)

    submissions = ContactSubmission.objects.all().order_by("-created_at")
    serializer = ContactSubmissionSerializer(submissions, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAdminUser])
def contact_detail(request, pk):
    submission = get_object_or_404(ContactSubmission, pk=pk)

    if request.method == "GET":
        serializer = ContactSubmissionSerializer(submission)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ContactSubmissionSerializer(submission, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    submission.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)