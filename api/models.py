from django.db import models


class Book(models.Model):
    title = models.CharField('Название книги', max_length=50)
    published_year = models.IntegerField('Год издания')
    genre = models.CharField('Жанр книги', max_length=50)
    rating = models.FloatField('Рейтинг книги')

    is_deleted = models.BooleanField('Безопасное удаление книги', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    name = models.CharField('Имя автора', max_length=50)

    is_deleted = models.BooleanField('Безопасное удаление автора', default=False)

    books = models.ManyToManyField(Book, related_name='authors', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
