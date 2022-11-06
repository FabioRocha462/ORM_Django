from django.db import models
from client.models import Client
# Create your models here.

class Address(models.Model):
    locality = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    cep = models.CharField(max_length=15)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)

    def __str__(self):
        return self.client.name