from rest_framework.generics import CreateAPIView

from .serializers import SupportServiceRequestSerializer


class SupportServiceRequestView(CreateAPIView):
    """Sending a request to the support service"""

    serializer_class = SupportServiceRequestSerializer

