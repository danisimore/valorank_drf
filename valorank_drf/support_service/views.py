from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import SupportServiceRequestSerializer
from .models import Request


class SupportServiceViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    queryset = Request.objects.all()
    serializer_class = SupportServiceRequestSerializer


