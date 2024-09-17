from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=225)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=225,default="uncategorized")
    price = models.IntegerField()
    description = models.TextField()