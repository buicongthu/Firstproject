from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255,null=False)
    address = models.CharField(null=False,max_length=255)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)


 