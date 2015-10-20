from rest_framework import serializers
from models import *

class VerseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Verse

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book