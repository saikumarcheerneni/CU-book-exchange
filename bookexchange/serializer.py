# bookexchange/serializers.py
from rest_framework import serializers
from .models import Textbook

class TextbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = ['id', 'title', 'author', 'edition', 'condition', 'course_code', 'available']
