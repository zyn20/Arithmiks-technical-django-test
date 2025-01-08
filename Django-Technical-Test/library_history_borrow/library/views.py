
from rest_framework import generics
from rest_framework.response import Response
from .models import Reader
from .serializers import ReaderSerializer
from django.db.models import Prefetch

class ReaderBorrowHistoryView(generics.RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_object(self):
        reader_id = self.kwargs['pk']
        books_borrowed = BorrowedBook.objects.select_related('book')
        borrowed_books_with_authors = books_borrowed.prefetch_related('book__authors')

        reader = Reader.objects.prefetch_related(
            Prefetch('borrowed_books', queryset= borrowed_books_with_authors )
        ).get(pk=reader_id)
        return reader