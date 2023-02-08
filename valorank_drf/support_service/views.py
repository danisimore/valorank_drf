from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import SupportServiceRequestSerializer
from .services import get_requests


class SupportServiceViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    queryset = get_requests()
    serializer_class = SupportServiceRequestSerializer


