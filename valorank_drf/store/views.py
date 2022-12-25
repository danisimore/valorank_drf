from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class ProductListView(APIView):
    """Вывод всех товаров"""

    @staticmethod
    def get(request):
        products = models.Product.objects.all()
        serializer = serializers.ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Вывод определенного товара"""

    @staticmethod
    def get(request, pk):
        product = models.Product.objects.get(id=pk)
        serializer = serializers.ProductDetailSerializer(product)
        return Response(serializer.data)
