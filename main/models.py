from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=225)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=225,default="uncategorized")
    price = models.IntegerField()
    description = models.TextField()