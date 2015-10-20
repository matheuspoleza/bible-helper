from django.db import models

class Book(models.Model):
	TESTAMENT_CHOICES = (
		('old', 'Velho Testamento'),
		('new', 'Novo Testamento')
	)
	cod = models.CharField(max_length=2,primary_key=True)
	name = models.CharField(max_length=50)
	short_name = models.CharField(max_length=2)
	testament = models.CharField(max_length=3, choices=TESTAMENT_CHOICES)

	def __unicode__(self):
		return self.name

class Version(models.Model):
	cod = models.CharField(max_length=3, primary_key=True)
	name = models.CharField(max_length=128)
	language = models.CharField(max_length=2)

	def __unicode__(self):
		return self.name

class Verse(models.Model):
	cod = models.CharField(max_length=5, primary_key=True)
	bible_version = models.ForeignKey(Version)
	book = models.ForeignKey(Book)
	number = models.IntegerField()
	chapter = models.IntegerField()
	text = models.TextField()

	def __unicode__(self):
		return self.book.short_name + ' ' + str(self.chapter) + ':' + str(self.number)