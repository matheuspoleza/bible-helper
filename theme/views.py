from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from models import *

class ThemeViewSet(viewsets.ModelViewSet):
	queryset = Theme.objects.all()
	serializer_class = ThemeSerializer