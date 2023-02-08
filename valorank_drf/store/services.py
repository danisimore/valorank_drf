from django_filters import rest_framework as filters
from .models import Product, BaseRank, DesiredRank


class CharFiletInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    base_rank = CharFiletInFilter(field_name='base_rank__title', lookup_expr='in')
    discount = filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['base_rank', 'discount']


def get_bestsellers():
    bestsellers = Product.objects.filter(is_bestseller=True)[:3].only(
        'title',
        'current_price',
        'image'
    )
    return bestsellers


def get_all_products():
    all_products = Product.objects.all().prefetch_related('base_rank', 'desired_rank')
    return all_products


def get_base_ranks():
    base_ranks = BaseRank.objects.all()
    return base_ranks


def get_desired_ranks():
    desired_ranks = DesiredRank.objects.all()
    return desired_ranks
