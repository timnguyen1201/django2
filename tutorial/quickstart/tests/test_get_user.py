from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class MeApiTests(APITestCase):
    def test_user_get(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.get(f'/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('email', response.data)

    def test_not_auth_user_get(self):
        User.objects.create(username="username", email="tim@gmail.com")
        response = self.client.get(f'/me/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
