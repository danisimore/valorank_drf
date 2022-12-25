from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """Список всех товаров"""

    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'old_price', 'current_price', 'execution_time')


class ProductDetailSerializer(serializers.ModelSerializer):
    """Определенный товар"""

    base_rank = serializers.SlugRelatedField(slug_field='title', read_only=True)
    desired_rank = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
