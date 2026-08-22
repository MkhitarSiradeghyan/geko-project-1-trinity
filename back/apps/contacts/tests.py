from rest_framework.test import APITestCase
from rest_framework import status


class ContactSubmissionTests(APITestCase):
    url = "/api/contacts/"

    def test_submission_with_email_only(self):
        response = self.client.post(self.url, {"email": "test@example.com"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_submission_with_phone_only(self):
        response = self.client.post(self.url, {"phone": "+37412345678"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_submission_with_both(self):
        response = self.client.post(self.url, {
            "email": "test@example.com",
            "phone": "+37412345678",
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rejected_without_email_or_phone(self):
        response = self.client.post(self.url, {"name": "John Doe"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)