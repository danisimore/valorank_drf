from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCategoryListView, ArticleDestroyView

urlpatterns = [
    path('all/', ArticleListView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
    path('destroy/<int:pk>/', ArticleDestroyView.as_view()),
    path('categories/', ArticleCategoryListView.as_view())
]
