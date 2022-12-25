from django_filters import rest_framework as filters

from .models import Article


class CharFiletInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ArticleFilter(filters.FilterSet):
    category = CharFiletInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Article
        fields = ['category']
