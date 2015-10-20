from rest_framework import serializers
from models import *

class ThemeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Theme