from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

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


class ArticleDestroyView(DestroyAPIView):
    """Удаление статьи"""
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ArticleCategoryListView(ListAPIView):
    """Вывод категорий"""

    queryset = ArticleCategory.objects.all()
    serializer_class = serializers.ArticleCategoryListSerializer
