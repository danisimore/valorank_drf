from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'base_ranks', views.BaseRankViewSet)
router.register(r'desired_ranks', views.DesiredRankViewSet)

urlpatterns = router.urls
