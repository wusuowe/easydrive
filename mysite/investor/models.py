from django.db import models
class Magic(models.Model):
    code = models.CharField(max_length=6)
    rdate = models.DateField()
    name = models.CharField(max_length=16)
    industry = models.CharField(max_length=64)
    roic = models.FloatField(default=0.0)
    rotc = models.FloatField(default=0.0)
    roicrank =models.IntegerField(default=0)
    rotcrank =models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    class Meta:
        unique_together = ('code','rdate')
# Create your models here.
