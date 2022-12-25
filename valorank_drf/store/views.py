from rest_framework.generics import ListAPIView, RetrieveAPIView

from . import models
from . import serializers


class ProductListView(ListAPIView):
    """Вывод всех товаров"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    """Вывод определенного товара"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
