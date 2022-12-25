from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCategoryListView

urlpatterns = [
    path('all/', ArticleListView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
    path('categories/', ArticleCategoryListView.as_view())
]
