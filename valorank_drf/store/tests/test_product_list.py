from rest_framework import status

from .setup import StoreSetUp


class TestProductList(StoreSetUp):

    def test_product_list(self):
        response = self.client.get('/api/v1/store/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
