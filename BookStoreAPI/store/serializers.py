from rest_framework import serializers

from .models import Genre, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            'author_name',
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )


class GenreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "books",
        )
