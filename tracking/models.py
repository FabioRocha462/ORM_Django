from django.db import models
from request.models import Request
# Create your models here.
class Tracking(models.Model):
    cod = models.UUIDField()
    request = models.ForeignKey(Request, on_delete = models.CASCADE)

    def __str__(self):
        return self.cod
