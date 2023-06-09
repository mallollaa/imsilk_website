from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=225)
    description= models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)