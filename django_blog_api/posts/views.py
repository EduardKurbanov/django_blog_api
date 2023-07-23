from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Article,Author
from .serializers import ArticleSerializer, AuthorSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorArticlesView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Article.objects.filter(authors__id=author_id)

