from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class MeApiPost(APITestCase):
    def test_user_post(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.post(f'/users/', {'username': 'tim', 'email': 'nguyenletu2010@gmail.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        new_user = User.objects.filter(username='tim')
        self.assertEqual(len(new_user), 1)
        new_user = new_user[0]
        self.assertEqual(new_user.email, 'nguyenletu2010@gmail.com')
