from .models import BooksAPI
from rest_framework import generics
from .serializers import BooksSerializer


class BookList(generics.ListCreateAPIView):
    queryset = BooksAPI.objects.all()
    serializer_class = BooksSerializer


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BooksAPI.objects.all()
    serializer_class = BooksSerializer
