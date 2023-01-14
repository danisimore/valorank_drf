from .setup import SetUpMainPageDataTest
from django.urls import reverse
from rest_framework import status


class TestArticles(SetUpMainPageDataTest):

    def test_main_page_articles(self):
        """Проверяем, что выводятся только 5 статей"""

        response = self.client.get(reverse('main_page_articles'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
