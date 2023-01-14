from rest_framework import status

from store.tests.setup import StoreSetUp


class TestProductDetail(StoreSetUp):

    def test_product_detail(self):
        """Делаем запрос на страницу с товаром, который существует"""

        response = self.client.get(f'/api/v1/store/products/{self.test_product.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Product')

    def test_fail_product_detail(self):
        """Делаем запрос на страницу с товаром, который не существует"""

        response = self.client.get('/api/v1/store/products/50/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
