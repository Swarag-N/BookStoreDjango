from django.shortcuts import render

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
