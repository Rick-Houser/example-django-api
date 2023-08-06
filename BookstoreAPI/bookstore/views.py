from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


"""
    API view for listing all books and creating new books.

    - `queryset`: Retrieves all Book objects from the database.
    - `serializer_class`: Uses the BookSerializer to serialize Book data.
"""
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""
    API view for retrieving, updating, and deleting a specific book.

    - `queryset`: Retrieves all Book objects from the database.
    - `serializer_class`: Uses the BookSerializer to serialize Book data.
"""
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
