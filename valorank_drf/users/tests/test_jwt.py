from .setup import TestAuthentication
from rest_framework import status


class TestJWT(TestAuthentication):

    def test_create_jwt(self):
        response = self.client.post('/auth/jwt/create/', {'email': 'test@email.tst', 'password': 'TestPassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_create_jwt(self):
        self.test_user.is_active = False
        self.test_user.save()
        response = self.client.post('/auth/jwt/create/', {'email': 'test@email.tst', 'password': 'TestPassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_jwt_refresh(self):
        response = self.client.post('/auth/jwt/create/', {'email': 'test@email.tst', 'password': 'TestPassword'})
        refresh_response = self.client.post('/auth/jwt/refresh/', {'refresh': response.data['refresh']})
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)

    def test_invalid_jwt_refresh(self):
        refresh_response = self.client.post('/auth/jwt/refresh/', {'refresh': 'vcxvCXVVVWE12fVdvgvVBB!@'})
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_jwt_verify(self):
        response = self.client.post('/auth/jwt/create/', {'email': 'test@email.tst', 'password': 'TestPassword'})
        verify_response = self.client.post('/auth/jwt/verify/', {'token': response.data['access']})
        self.assertEqual(verify_response.status_code, status.HTTP_200_OK)

    def test_invalid_jwt_verify(self):
        response = self.client.post('/auth/jwt/verify/', {'token': '123QWE'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)