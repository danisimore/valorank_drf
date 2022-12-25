from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ArticleListSerializer, ArticleDetailSerializer, ArticleCategoryListSerializer
from .models import Article, ArticleCategory


class ArticleListView(APIView):
    """Вывод всех статей"""

    @staticmethod
    def get(request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    """Вывод определенной статьи"""

    @staticmethod
    def get(request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)


class ArticleCategoryListView(APIView):
    """Вывод категорий"""

    @staticmethod
    def get(request):
        category = ArticleCategory.objects.all()
        serializer = ArticleCategoryListSerializer(category, many=True)
        return Response(serializer.data)
