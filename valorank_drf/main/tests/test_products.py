from .setup import SetUpMainPageDataTest
from django.urls import reverse
from rest_framework import status


class TestProducts(SetUpMainPageDataTest):
    def test_main_page_products(self):
        """Проверяем, что выводятся только 3 товара, у которых поле is_bestseller=True"""

        response = self.client.get(reverse('main_page_products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
