from django.db import models


class Pantry(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=50)
    expiration = models.DateField(null=True)
    alert = models.BooleanField(null=False)



