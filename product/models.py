from django.db import models
from store.models import Store
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    unitary_value = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name