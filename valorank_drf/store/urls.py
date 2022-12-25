from django.urls import path

from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('products/all/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view())
]
