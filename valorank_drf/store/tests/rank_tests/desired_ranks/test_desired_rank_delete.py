from rest_framework import status

from store.tests.setup import StoreSetUp


class TestBaseRankDelete(StoreSetUp):

    def test_delete_by_an_unauthorized_user(self):
        response = self.client.delete(f'/api/v1/store/desired_ranks/{self.test_desired_rank.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_by_a_non_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/', {'email': 'simple@user.tst', 'password': 'Password!123'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.delete(f'/api/v1/store/desired_ranks/{self.test_desired_rank.pk}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_by_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/', {'email': 'super@user.tst', 'password': 'Password!123'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.delete(f'/api/v1/store/desired_ranks/{self.test_desired_rank.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
