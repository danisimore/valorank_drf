from rest_framework import status

from . import setup


class ArticleListTest(setup.ArticleTests):

    def test_article_list(self):
        response = self.client.get('/api/v1/articles/data/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
