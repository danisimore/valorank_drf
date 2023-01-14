from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.HomeProductListView.as_view(), name='main_page_products'),
    path('articles/', views.HomeArticleListView.as_view(), name='main_page_articles'),
    path('best_busters/', views.BusterListView.as_view(), name='best_boosters')
]
