from django.db import models
from request.models import Request
from product.models import Product
# Create your models here.

class Request_Product(models.Model):
    quantity = models.IntegerField()
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name