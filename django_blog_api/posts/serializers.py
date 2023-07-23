from rest_framework import serializers
from .models import Article, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()

    class Meta:
        model = Article
        fields = '__all__'



