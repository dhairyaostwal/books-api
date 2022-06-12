from django.shortcuts import render
from .models import BooksAPI
from rest_framework import generics, mixins
from .serializers import BooksSerializer


class BookList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = BooksAPI.objects.all()
    serializer_class = BooksSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
