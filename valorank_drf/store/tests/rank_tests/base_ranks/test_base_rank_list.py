from rest_framework import status

from store.tests.setup import StoreSetUp


class TestBaseRankList(StoreSetUp):

    def test_base_rank_list(self):
        response = self.client.get('/api/v1/store/base_ranks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
