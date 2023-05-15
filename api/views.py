from django.shortcuts import render
from .serializers import BooksSerializer,ClothesSerializer,MiscSerializer
from resources.models import Book,Clothes,Miscellaneous
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def BooksAPI(request):
    books = Book.objects.all().order_by('donated')
    serialized_data = BooksSerializer(books,many=True)
    json_data = JSONRenderer().render(serialized_data.data)
    return HttpResponse(json_data, content_type='application/json')


def ClothesAPI(request):
    books = Clothes.objects.all().order_by('donated')
    serialized_data = ClothesSerializer(books,many=True)
    json_data = JSONRenderer().render(serialized_data.data)
    return HttpResponse(json_data, content_type='application/json')


def MiscAPI(request):
    books = Miscellaneous.objects.all().order_by('donated')
    serialized_data = MiscSerializer(books,many=True)
    json_data = JSONRenderer().render(serialized_data.data)
    return HttpResponse(json_data, content_type='application/json')