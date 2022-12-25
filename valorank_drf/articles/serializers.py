from rest_framework import serializers

from .models import Article, ArticleCategory


class ArticleListSerializer(serializers.ModelSerializer):
    """Список всех статей"""

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'category', 'image')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Определенная статья"""

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategoryListSerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = ArticleCategory
        fields = ('id', 'title')
