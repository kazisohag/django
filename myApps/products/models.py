from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    descripssion = models.TextField()
    price = models.FloatField()
    status = models.BooleanField()