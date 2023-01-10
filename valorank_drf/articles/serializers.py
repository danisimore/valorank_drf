from rest_framework import serializers

from .models import Article, ArticleCategory


class ArticleSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field='title', queryset=ArticleCategory.objects.all())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = '__all__'
