from .setup import TestAuthentication
from rest_framework import status


class TestPasswordReset(TestAuthentication):

    def test_password_reset(self):
        response = self.client.post('/auth/users/reset_password/', {'email': self.test_user.email})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_password_reset_confirm(self):
        response = self.client.post('/auth/users/reset_password_confirm/', self.extra_data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_password_reset_confirm(self):
        response = self.client.post('/auth/users/reset_password_confirm/', {'invalid': 'data'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
