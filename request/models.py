from django.db import models
from client.models import Client
from store.models import Store
# Create your models here.

class Request(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name
