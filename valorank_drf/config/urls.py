from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

from . import settings


schema_view = get_swagger_view(title='Valorank API')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('users.urls')),
    path('auth/', include('config.jwt')),

    path('api/v1/main/', include('main.urls')),
    path('api/v1/store/', include('store.urls')),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/support_service/', include('support_service.urls')),

    path('swagger/', schema_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
