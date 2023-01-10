from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from . import serializers
from .models import Article, ArticleCategory


class ArticleViewSet(ModelViewSet):

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleCategoryViewSet(ModelViewSet):

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]

        return super().get_permissions()

    queryset = ArticleCategory.objects.all()
    serializer_class = serializers.ArticleCategorySerializer
