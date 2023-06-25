from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class MeApiTests(APITestCase):
    def test_user_patch(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.patch(f'/users/{user.id}/', {'email': 'nguyen@gmail.com'})
        user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        # assert user data to make sure email is updated
        self.assertEqual(len(response.data), 4)
        self.assertIn('email', response.data)
        self.assertEqual(user.email, "nguyen@gmail.com")
