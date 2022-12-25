from rest_framework.generics import ListAPIView, RetrieveAPIView

from . import serializers
from .models import Article, ArticleCategory


class ArticleListView(ListAPIView):
    """Вывод всех статей"""

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer


class ArticleDetailView(RetrieveAPIView):
    """Вывод определенной статьи"""

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer


class ArticleCategoryListView(ListAPIView):
    """Вывод категорий"""

    queryset = ArticleCategory.objects.all()
    serializer_class = serializers.ArticleCategoryListSerializer
