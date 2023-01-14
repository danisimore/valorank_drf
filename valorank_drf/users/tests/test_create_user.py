from .setup import TestAuthentication
from rest_framework import status


class TestCreateUser(TestAuthentication):

    def test_create_user(self):
        response = self.client.post('/auth/users/', self.valid_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_user(self):
        self.client.post('/auth/users/', self.valid_user_data)
        response = self.client.post('/auth/users/', self.valid_user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_invalid_data(self):
        response = self.client.post('/auth/users/', self.invalid_user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
