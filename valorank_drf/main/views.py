from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Product
from articles.models import Article

from . import serializers


class HomeProductListView(APIView):
    """Вывод товаров с главной страницы"""

    @staticmethod
    def get(request):
        products = Product.objects.filter(is_bestseller=True)[:3]
        serializer = serializers.HomeProductListSerializer(products, many=True)
        return Response(serializer.data)


class HomeArticleListView(APIView):
    """Вывод статей с главной страницы"""

    @staticmethod
    def get(request):
        articles = Article.objects.all().order_by('-pk')[:5]
        serializer = serializers.HomeArticleListSerializer(articles, many=True)
        return Response(serializer.data)
