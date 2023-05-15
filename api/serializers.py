from rest_framework import serializers
from resources.models import Book,Clothes,Miscellaneous

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','desc','rating','image','classno','orgn','address','donated']

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['title','desc','rating','image','orgn','address','donated']

class MiscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miscellaneous
        fields = ['title','desc','rating','image','orgn','address','donated']