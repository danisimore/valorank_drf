from rest_framework import status

from . import base


class ArticleDetailTest(base.ArticleTests):

    def test_article_detail(self):
        response = self.client.get(f'/api/v1/articles/data/{self.lonely_article.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test article')

    def test_fail_article_detail(self):
        response = self.client.get('/api/v1/articles/data/50/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
