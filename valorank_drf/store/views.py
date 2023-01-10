from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import (
    Product,
    BaseRank,
    DesiredRank
)

from . import serializers
from articles.views import ArticleViewSet  # Для того чтобы не переопределять get_permissions


class ProductViewSet(ArticleViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class BaseRankViewSet(ArticleViewSet):
    queryset = BaseRank.objects.all()
    serializer_class = serializers.BaseRankSerializer


class DesiredRankViewSet(ProductViewSet):
    queryset = DesiredRank.objects.all()
    serializer_class = serializers.DesiredRankSerializer
