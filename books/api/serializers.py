from dataclasses import fields
from rest_framework import serializers
from api.models import BooksAPI


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAPI
        fields = ['id', 'title', 'author', 'description', 'img_url']
