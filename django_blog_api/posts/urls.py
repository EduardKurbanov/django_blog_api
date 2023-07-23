from django.urls import path
from .views import ArticleListCreateView, ArticleRetrieveUpdateDeleteView

urlpatterns = [
    path('/articles/', ArticleListCreateView.as_view(), name='article_list_create'),
    path('/articles/<int:pk>/', ArticleRetrieveUpdateDeleteView.as_view(), name='article_retrieve_update_delete'),
]