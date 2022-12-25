from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .service import ArticleFilter
from .models import Article, ArticleCategory


class ArticleListView(ListAPIView):
    """Вывод всех статей"""

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticleFilter


class ArticleDetailView(RetrieveAPIView):
    """Вывод определенной статьи"""

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer


class ArticleCategoryListView(ListAPIView):
    """Вывод категорий"""

    queryset = ArticleCategory.objects.all()
    serializer_class = serializers.ArticleCategoryListSerializer
