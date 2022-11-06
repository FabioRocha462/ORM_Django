from django.db import models
from store.models import Store
from request.models import Request
from address.models import Address
# Create your models here.

class Delivery(models.Model):
    status_delivery  = (
        ("Yes","delivery"),
        ("No", "no delivery"),
    )
    date = models.DateField(auto_now_add=True)
    date_delivery = models.DateTimeField()
    status = models.CharField(max_length=100, choices = status_delivery)
    shipping_value = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.store.name
