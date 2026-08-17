from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from .models import FaqEntry
from .serializers import FaqEntrySerializer


class FaqModelTests(APITestCase):

    def test_default_values(self):
        faq = FaqEntry.objects.create(
            question="What is Trinity Travel?",
            answer="A travel agency.",
        )

        self.assertTrue(faq.is_active)
        self.assertEqual(faq.ordering, 0)
        self.assertIsNotNone(faq.created_at)
        self.assertIsNotNone(faq.updated_at)


class FaqSerializerTests(APITestCase):

    def test_serializer_output(self):
        faq = FaqEntry.objects.create(
            question="What is Trinity Travel?",
            answer="A travel agency.",
            is_active=True,
            ordering=1,
        )

        serializer = FaqEntrySerializer(faq)

        self.assertEqual(
            serializer.data,
            {
                "id": faq.id,
                "question": "What is Trinity Travel?",
                "answer": "A travel agency.",
            },
        )


class FaqPermissionTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="regular_user",
            password="password123",
        )

        self.staff_user = User.objects.create_user(
            username="staff_user",
            password="password123",
            is_staff=True,
        )

        self.active_faq = FaqEntry.objects.create(
            question="Active question",
            answer="Active answer",
            is_active=True,
            ordering=1,
        )

        self.inactive_faq = FaqEntry.objects.create(
            question="Inactive question",
            answer="Inactive answer",
            is_active=False,
            ordering=2,
        )

    def test_anonymous_can_list_active_faqs(self):
        response = self.client.get("/api/faq/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            1,
        )

        self.assertEqual(
            response.data[0]["question"],
            "Active question",
        )

    def test_anonymous_faqs_are_ordered(self):
        FaqEntry.objects.create(
            question="First",
            answer="First answer",
            ordering=0,
        )

        FaqEntry.objects.create(
            question="Second",
            answer="Second answer",
            ordering=10,
        )

        response = self.client.get("/api/faq/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        questions = [
            item["question"]
            for item in response.data
        ]

        self.assertEqual(
            questions,
            [
                "First",
                "Active question",
                "Second",
            ],
        )

    def test_anonymous_cannot_see_inactive_detail(self):
        response = self.client.get(
            f"/api/faq/{self.inactive_faq.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_anonymous_cannot_create(self):
        response = self.client.post(
            "/api/faq/",
            {
                "question": "New question",
                "answer": "New answer",
            },
            format="json",
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

    def test_authenticated_non_staff_cannot_create(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.post(
            "/api/faq/",
            {
                "question": "New question",
                "answer": "New answer",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_staff_can_see_inactive_faqs(self):
        self.client.force_authenticate(
            user=self.staff_user,
        )

        response = self.client.get("/api/faq/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            2,
        )

    def test_staff_can_create_faq(self):
        self.client.force_authenticate(
            user=self.staff_user,
        )

        response = self.client.post(
            "/api/faq/",
            {
                "question": "New question",
                "answer": "New answer",
                "is_active": False,
                "ordering": 3,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            FaqEntry.objects.filter(
                question="New question",
            ).exists()
        )

    def test_staff_can_update_faq(self):
        self.client.force_authenticate(
            user=self.staff_user,
        )

        response = self.client.put(
            f"/api/faq/{self.inactive_faq.id}/",
            {
                "question": "Updated question",
                "answer": "Updated answer",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.inactive_faq.refresh_from_db()

        self.assertEqual(
            self.inactive_faq.question,
            "Updated question",
        )

    def test_staff_can_delete_faq(self):
        self.client.force_authenticate(
            user=self.staff_user,
        )

        response = self.client.delete(
            f"/api/faq/{self.inactive_faq.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(
            FaqEntry.objects.filter(
                id=self.inactive_faq.id,
            ).exists()
        )