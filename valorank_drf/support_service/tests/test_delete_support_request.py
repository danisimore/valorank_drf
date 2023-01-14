from .setup import TestSupportService

from rest_framework import status


class TestDeleteSupportRequest(TestSupportService):

    def test_delete_by_unauthorized_user(self):
        response = self.client.delete('/api/v1/support_service/request/', self.support_request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_by_a_non_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/',
                                     {'email': 'simple@user.test', 'password': 'SimpleUserPassword'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.delete(f'/api/v1/support_service/request/{self.test_request.pk}/', self.support_request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_by_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/', {'email': 'super@user.test', 'password': 'SuperUserPassword'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.delete(f'/api/v1/support_service/request/{self.test_request.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
