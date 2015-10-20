from django.db import models
from bible.models import Verse

class Theme(models.Model):
	name = models.CharField(max_length=128)
	verses = models.ManyToManyField(Verse)

	def __unicode__(self):
		return self.name