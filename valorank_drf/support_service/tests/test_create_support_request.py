from .setup import TestSupportService

from rest_framework import status


class TestCreateSupportRequest(TestSupportService):

    def test_create_support_request(self):
        response = self.client.post('/api/v1/support_service/request/', self.support_request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_support_request(self):
        response = self.client.post('/api/v1/support_service/request/', self.invalid_support_request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
