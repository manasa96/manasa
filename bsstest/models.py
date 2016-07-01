from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# Create your models here.

class bss(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password=models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    def __unicode__(self):
        return smart_unicode(self.first_name)

