from rest_framework.generics import ListAPIView

from store.models import Product
from articles.models import Article
from users.models import User

from . import serializers


class HomeProductListView(ListAPIView):
    """Products from the main page"""

    queryset = Product.objects.filter(is_bestseller=True)[:3].only(
        'title',
        'current_price',
        'image'
    )
    serializer_class = serializers.HomeProductListSerializer


class HomeArticleListView(ListAPIView):
    """Articles from the home page"""

    queryset = Article.objects.all().order_by('-pk')[:5].prefetch_related('category').only(
        'title',
        'category',
        'image'
    )
    serializer_class = serializers.HomeArticleListSerializer


class BusterListView(ListAPIView):
    """The best boosters"""

    queryset = User.objects.filter(is_best=True).prefetch_related('mailbox').only(
        'avatar',
        'mailbox'
    )
    serializer_class = serializers.AboutBusterListSerializer
