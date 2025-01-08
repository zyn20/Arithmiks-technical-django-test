from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')

class Reader(models.Model):
    name = models.CharField(max_length=255)

class BorrowedBook(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed_books')
    borrowed_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)