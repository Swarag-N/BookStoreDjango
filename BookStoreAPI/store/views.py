from django.shortcuts import render
from django.http import Http404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class LatestBooksList(APIView):
    def get(self, request, format=None):
        products = Book.objects.all()[0:4]
        serializer = BookSerializer(products, many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    def get_object(self, genre_slug, book_slug):
        try:
            return Book.objects.filter(category__slug=genre_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, genre_slug, book_slug, format=None):
        book = self.get_object(genre_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class GenreDetail(APIView):
    def get_object(self, genre_slug):
        try:
            return Genre.objects.get(slug=genre_slug)
        except Genre.DoesNotExist:
            raise Http404
    
    def get(self, request, genre_slug, format=None):
        genre_instance = self.get_object(genre_slug)
        serializer = GenreSerializer(genre_instance)
        return Response(serializer.data)

