from django.db import models
from store.models import Store
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name