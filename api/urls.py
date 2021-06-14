from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/top', views.TopBookListView.as_view(), name='top_books_'),
    path('books/year/', views.BookByYearListView.as_view(), name='books_by_year'),
    path('authors/top/', views.TopAuthorListView.as_view(), name='top_authors'),
    path('genres/', views.GenreBookListView.as_view(), name='genres'),
    path('find_by_authors/', views.ByNameAuthorListView.as_view(), name='books_by_author'),
    path('books/<int:pk>', views.SoftDeleteBookView.as_view(), name='soft_delete_book'),
    path('authors/<int:pk>', views.SoftDeleteAuthorView.as_view(), name='soft_delete_author')
]
