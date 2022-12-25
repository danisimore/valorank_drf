from rest_framework import serializers

from articles.models import Article
from store.models import Product


class HomeProductListSerializer(serializers.ModelSerializer):
    """Список товаров с главной страницы"""

    class Meta:
        model = Product
        fields = ('pk', 'title', 'current_price', 'image')


class HomeArticleListSerializer(serializers.ModelSerializer):
    """Список товаров с главной страницы"""

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'title', 'category', 'image')
