from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from django.db.models import Count
from random import randint

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer,\
    CountBookAuthorSerializer, GenreBookSerializer


def get_names(names):
    """
    Returns pairs 'Firstname Lastname' of the authors.
    """
    names = names.split(' ')
    lst = []
    for i in range(0, len(names), 2):
        lst.append(' '.join(names[i:i + 2]))
    return lst


def get_header():
    """
    Return X-Test-Header with random number.
    """
    return {'X-Test-Header': randint(1, 100)}


class BookListView(APIView):
    """
    Returns list of books.
    """
    def get(self, request):
        books = Book.objects.filter(is_deleted=False)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, headers=get_header())


class AuthorListView(APIView):
    """
    Returns list of authors.
    """
    def get(self, request):
        authors = Author.objects.filter(is_deleted=False)
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, headers=get_header())


class TopBookListView(APIView):
    """
    Returns top 10 books with highest rating.
    """
    def get(self, request):
        books = Book.objects.filter(is_deleted=False).order_by('-rating')[:10]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, headers=get_header())


class BookByYearListView(APIView):
    """
    Returns list of books in given years range.
    """
    def get(self, request):
        year_from = request.query_params.get('from')
        year_to = request.query_params.get('to')

        if year_from and year_to:
            books = Book.objects.filter(published_year__gte=year_from,
                                        published_year__lte=year_to,
                                        is_deleted=False)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, headers=get_header())
        return Response(status=status.HTTP_400_BAD_REQUEST, headers=get_header())


class TopAuthorListView(APIView):
    """
    Returns top 10 authors with the biggest amount of books.
    """
    def get(self, request):
        authors = Author.objects.filter(is_deleted=False).annotate(books_amount=Count('books'))\
                      .order_by('-books_amount')[:10]
        serializer = CountBookAuthorSerializer(authors, many=True)
        return Response(serializer.data, headers=get_header())


class GenreBookListView(APIView):
    """
    Returns list of genres with amount of books in it.
    """
    def get(self, request):
        books = Book.objects.values('genre').filter(is_deleted=False).annotate(books_amount=Count('id'))\
            .order_by('genre')
        serializer = GenreBookSerializer(books, many=True)
        return Response(serializer.data, headers=get_header())


class ByNameAuthorListView(APIView):
    """
    Returns list of authors with given names.
    """
    def get(self, request):
        names = request.query_params.get('q')

        print(get_names(names))
        if names:
            books = Book.objects.filter(authors__name__in=get_names(names),
                                        is_deleted=False)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, headers=get_header())
        return Response(status=status.HTTP_400_BAD_REQUEST, headers=get_header())


class SoftDeleteBookView(APIView):
    """
    Soft delete of a book with given id.
    """
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        if book:
            book.is_deleted = True
            book.save()
            return Response(status=status.HTTP_200_OK, headers=get_header())
        return Response(status=status.HTTP_404_NOT_FOUND, headers=get_header())


class SoftDeleteAuthorView(APIView):
    """
    Soft delete of a author with given id.
    """
    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        if author:
            author.is_deleted = True
            author.save()
            return Response(status=status.HTTP_200_OK, headers=get_header())
        return Response(status=status.HTTP_404_NOT_FOUND, headers=get_header())
