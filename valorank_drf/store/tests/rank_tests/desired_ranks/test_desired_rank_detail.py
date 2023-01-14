from rest_framework import status

from store.tests.setup import StoreSetUp


class TestBaseRankDetail(StoreSetUp):

    def test_base_rank_detail(self):
        response = self.client.get(f'/api/v1/store/desired_ranks/{self.test_desired_rank.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Desired Rank')
