from rest_framework_simplejwt.views import TokenObtainPairView as RestTokenObtainPairView
from . import serializers


class TokenObtainPairView(RestTokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer

