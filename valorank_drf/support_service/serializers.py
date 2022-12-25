from rest_framework import serializers

from .models import Request


class SupportServiceRequestSerializer(serializers.ModelSerializer):
    """Отправка заявки в службу поддержки"""

    class Meta:
        model = Request
        fields = ('email', 'problem_description')
