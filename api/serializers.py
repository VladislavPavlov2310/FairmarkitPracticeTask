from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'published_year', 'genre', 'rating']


class CountBookAuthorSerializer(serializers.ModelSerializer):
    books_amount = serializers.IntegerField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'books_amount']


class GenreBookSerializer(serializers.ModelSerializer):
    books_amount = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['genre', 'books_amount']
