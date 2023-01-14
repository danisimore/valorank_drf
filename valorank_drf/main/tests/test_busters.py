from .setup import SetUpMainPageDataTest
from django.urls import reverse
from rest_framework import status


class TestBusters(SetUpMainPageDataTest):

    def test_about_best_busters(self):
        """Проверяем, что выводятся только те бустеры, у которых поле is_best=True"""

        response = self.client.get(reverse('best_boosters'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
