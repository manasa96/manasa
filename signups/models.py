from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    roll = models.CharField(max_length=40)
    def __unicode__(self):
        return smart_unicode(self.name)
