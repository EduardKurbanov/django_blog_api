from django.urls import path
from .views import ArticleListCreateView, ArticleRetrieveUpdateDeleteView, AuthorListCreateView, AuthorRetrieveUpdateDeleteView, AuthorArticlesView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author_list_create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDeleteView.as_view(), name='author_retrieve_update_delete'),
    path('articles/', ArticleListCreateView.as_view(), name='article_list_create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDeleteView.as_view(), name='article_retrieve_update_delete'),
    path('authors/<int:author_id>/articles/', AuthorArticlesView.as_view(), name='author_articles'),
]