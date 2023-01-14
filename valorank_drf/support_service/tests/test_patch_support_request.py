from .setup import TestSupportService

from rest_framework import status


class TestPatchSupportRequest(TestSupportService):

    def test_patch_by_an_unauthorized_user(self):
        response = self.client.patch('/api/v1/support_service/request/', self.support_request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_by_a_non_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/',
                                     {'email': 'simple@user.test', 'password': 'SimpleUserPassword'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.patch(f'/api/v1/support_service/request/{self.test_request.pk}/', self.support_request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_by_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/', {'email': 'super@user.test', 'password': 'SuperUserPassword'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.patch(f'/api/v1/support_service/request/{self.test_request.pk}/', self.support_request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
