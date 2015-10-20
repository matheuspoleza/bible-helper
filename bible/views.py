from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from models import *

class VerseViewSet(viewsets.ModelViewSet):
	queryset = Verse.objects.all()
	serializer_class = VerseSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer