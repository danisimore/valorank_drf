from django.urls import path

from .views import SupportServiceRequestView

urlpatterns = [
    path('request/', SupportServiceRequestView.as_view())
]
