from rest_framework import serializers

from .models import (
    Product,
    BaseRank,
    DesiredRank
)


class ProductSerializer(serializers.ModelSerializer):

    base_rank = serializers.SlugRelatedField(slug_field='title', queryset=BaseRank.objects.all())
    desired_rank = serializers.SlugRelatedField(slug_field='title', queryset=DesiredRank.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class BaseRankSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseRank
        fields = '__all__'


class DesiredRankSerializer(serializers.ModelSerializer):

    class Meta:
        model = DesiredRank
        fields = '__all__'
