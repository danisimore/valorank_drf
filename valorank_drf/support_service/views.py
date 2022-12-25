from rest_framework.generics import CreateAPIView

from .serializers import SupportServiceRequestSerializer


class SupportServiceRequestView(CreateAPIView):
    """Отправка заявки в службу поддержки"""

    serializer_class = SupportServiceRequestSerializer

