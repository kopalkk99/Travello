from django.db import models

# Create your models here.
class Destination(models.Model):
        destName = models.CharField(max_length=200)
        destDesc = models.TextField(2000)
        price = models.IntegerField()
        img = models.ImageField(upload_to='images')
        offer = models.BooleanField(default = False)
