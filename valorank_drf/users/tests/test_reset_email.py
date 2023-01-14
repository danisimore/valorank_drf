from .setup import TestAuthentication
from rest_framework import status


class TestEmailReset(TestAuthentication):

    def test_reset_email(self):
        response = self.client.post('/auth/users/reset_email/', {'email': self.test_user.email})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_reset_email_confirm(self):
        response = self.client.post('/auth/users/reset_email_confirm/', self.extra_data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_reset_email_confirm(self):
        response = self.client.post('/auth/users/reset_email_confirm/', {'uid': 'invalid', 'token': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
