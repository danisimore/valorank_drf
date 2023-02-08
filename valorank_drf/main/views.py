from rest_framework.generics import ListAPIView

from store.services import get_bestsellers

from articles.services import get_last_five_articles

from users.services import get_best_busters

from . import serializers


class HomeProductListView(ListAPIView):
    """Products from the main page"""

    queryset = get_bestsellers()
    serializer_class = serializers.HomeProductListSerializer


class HomeArticleListView(ListAPIView):
    """Articles from the home page"""

    queryset = get_last_five_articles()
    serializer_class = serializers.HomeArticleListSerializer


class BusterListView(ListAPIView):
    """The best boosters"""

    queryset = get_best_busters()
    serializer_class = serializers.AboutBusterListSerializer
