from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from . import serializers
from .service import ProductFilter

all_products = Product.objects.all()


class ProductListView(ListAPIView):
    """Вывод всех товаров"""

    queryset = all_products
    serializer_class = serializers.ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class ProductDetailView(RetrieveAPIView):
    """Вывод определенного товара"""

    queryset = all_products
    serializer_class = serializers.ProductDetailSerializer
