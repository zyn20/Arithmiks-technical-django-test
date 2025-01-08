
from rest_framework import serializers
from .models import Author, Book, Reader, BorrowedBook

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name',]

class BookSerializer(serializers.ModelSerializer):

    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors']

class BorrowedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    reader= ReaderSerializer()
    borrowed_date = serializers.DateField()
    returned_return = serializers.DateField(allow_null=True)

    class Meta:
        model = BorrowedBook
        fields = ['book', 'borrowed_date', 'returned_date', ]

class ReaderSerializer(serializers.ModelSerializer):
    borrowed_books = BorrowedBookSerializer(many=True)
    class Meta:
        model = Reader
        fields = ['id', 'name']
