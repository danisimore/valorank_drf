from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r'data', views.ArticleViewSet)
router.register(r'categories', views.ArticleCategoryViewSet)

urlpatterns = router.urls
