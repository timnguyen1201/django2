from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class TestUser(APITestCase):
    def test_user_get(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.get(f'/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert response data
        self.assertEqual(len(response.data), 4)
        self.assertIn('url', response.data)
        self.assertIn('username', response.data)
        self.assertIn('email', response.data)
        self.assertIn('groups', response.data)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['username'], user.username)

    def test_user_list(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.get(f'/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        first_user_data = response.data['results'][0]
        self.assertEqual(len(first_user_data), 4)
        self.assertIn('url', first_user_data)
        self.assertIn('username', first_user_data)
        self.assertIn('email', first_user_data)
        self.assertIn('groups', first_user_data)
        self.assertEqual(first_user_data['email'], user.email)
        self.assertEqual(first_user_data['username'], user.username)

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

    def test_user_put(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.put(f'/users/{user.id}/', {'username': 'username', 'email': 'nguyen@gmail.com'})
        user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        # assert user data to make sure email is updated
        self.assertEqual(len(response.data), 4)
        self.assertEqual(user.email, "nguyen@gmail.com")

    def test_user_delete(self):
        user = User.objects.create(username="username", email="tim@gmail.com")
        self.client.force_authenticate(user=user)
        response = self.client.delete(f'/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    # test delete all users
