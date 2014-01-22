#encoding=utf8
from django.db import models

# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=100)
	addr = models.CharField(max_length=200)
	rank = models.FloatField(default=0.0)
	@classmethod
	def get_select_list(cls):
		return [(o.id,o.name) for o in cls.objects.order_by('id')]
		
	
	def __unicode__(self):
		return self.name
class Coach(models.Model):
	name = models.CharField(max_length=50)
	sex = models.IntegerField(default=0,choices=((0,'女'),(1,'男')))
	school = models.ForeignKey(School)
	photo = models.ImageField(upload_to = 'photos')
	thumb = models.FilePathField(path='photos/thumb')
	rank = models.FloatField(default=0.0)
	def __unicode__(self):
		return self.name

