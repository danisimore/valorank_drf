from rest_framework import status

from . import base


class ArticleCreateTest(base.ArticleTests):

    def test_create_by_an_unauthorized_user(self):
        response = self.client.post('/api/v1/articles/data/', self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_by_a_non_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/', {'email': 'simple@user.tst', 'password': 'Password!123'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.post('/api/v1/articles/data/', self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_by_superuser(self):
        jwt_token = self.client.post('/auth/jwt/create/', {'email': 'super@user.tst', 'password': 'Password!123'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
        response = self.client.post('/api/v1/articles/data/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
