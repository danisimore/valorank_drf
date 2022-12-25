from django_filters import rest_framework as filters
from .models import Product


class CharFiletInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    base_rank = CharFiletInFilter(field_name='base_rank__title', lookup_expr='in')
    discount = filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['base_rank', 'discount']
