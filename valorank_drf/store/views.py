from articles.views import ArticleViewSet  # Для того чтобы не переопределять get_permissions

from . import serializers
from .services import get_all_products, get_base_ranks, get_desired_ranks


class ProductViewSet(ArticleViewSet):
    """Products"""
    queryset = get_all_products()
    serializer_class = serializers.ProductSerializer


class BaseRankViewSet(ArticleViewSet):
    """User rank"""
    queryset = get_base_ranks()
    serializer_class = serializers.BaseRankSerializer


class DesiredRankViewSet(ProductViewSet):
    """Rank to which a boost is needed"""
    queryset = get_desired_ranks()
    serializer_class = serializers.DesiredRankSerializer
