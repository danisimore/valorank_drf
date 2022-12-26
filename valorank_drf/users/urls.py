from django.urls import path
from .views import RegistrationAPIView

urlpatterns = [
    path('authentication', RegistrationAPIView.as_view())
]
