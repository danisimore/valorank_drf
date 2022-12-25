from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.HomeProductListView.as_view()),
    path('articles/', views.HomeArticleListView.as_view())
]
