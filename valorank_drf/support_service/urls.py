from rest_framework import routers
from .views import SupportServiceViewSet

router = routers.SimpleRouter()

router.register(r'request', SupportServiceViewSet)

urlpatterns = router.urls

