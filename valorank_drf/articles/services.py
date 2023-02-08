from django_filters import rest_framework as filters

from .models import Article, ArticleCategory


class CharFiletInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ArticleFilter(filters.FilterSet):
    category = CharFiletInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Article
        fields = ['category']


def get_all_articles():
    all_articles = Article.objects.all().prefetch_related('category')
    return all_articles


def get_last_five_articles():
    last_articles = Article.objects.all().order_by('-pk')[:5].prefetch_related('category').only(
        'title',
        'category',
        'image'
    )
    return last_articles

def get_all_article_categories():
    all_categories = ArticleCategory.objects.all()
    return all_categories
