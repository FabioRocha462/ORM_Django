from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20,unique = True)
    email = models.EmailField()

    def __str__(self):
        return self.name