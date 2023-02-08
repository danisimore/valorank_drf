from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from . import serializers
from .services import get_all_articles, get_all_article_categories


class ArticleViewSet(ModelViewSet):
    """Articles"""
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()

    queryset = get_all_articles()
    serializer_class = serializers.ArticleSerializer


class ArticleCategoryViewSet(ArticleViewSet):
    """Categories of articles"""
    queryset = get_all_article_categories()
    serializer_class = serializers.ArticleCategorySerializer
