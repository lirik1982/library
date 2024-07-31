from django.utils import timezone
from rest_framework import serializers
from .models import Book, Deal
from authentication.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre')


class DealSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    reader = UserSerializer()

    class Meta:
        model = Deal
        fields = ('id', 'book', 'reader', 'date_taken', 'date_get_back')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_since_taked'] = (timezone.now() - instance.date_taken).days
        representation.pop('date_get_back')
        return representation
