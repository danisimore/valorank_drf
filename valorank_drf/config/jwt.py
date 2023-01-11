from django.urls import re_path
from users.views import TokenObtainPairView
from rest_framework_simplejwt import views


urlpatterns = [
    re_path(r"^jwt/create/?", TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", views.TokenVerifyView.as_view(), name="jwt-verify"),
]