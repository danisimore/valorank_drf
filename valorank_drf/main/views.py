from rest_framework.generics import ListAPIView

from store.models import Product
from articles.models import Article
from users.models import User

from . import serializers


class HomeProductListView(ListAPIView):
    """Вывод товаров с главной страницы"""

    queryset = Product.objects.filter(is_bestseller=True)[:3]
    serializer_class = serializers.HomeProductListSerializer


class HomeArticleListView(ListAPIView):
    """Вывод статей с главной страницы"""

    queryset = Article.objects.all().order_by('-pk')[:5]
    serializer_class = serializers.HomeArticleListSerializer


class BusterListView(ListAPIView):
    """Вывод лучших бустеров"""

    queryset = User.objects.filter(is_best=True)
    serializer_class = serializers.AboutBusterListSerializer
