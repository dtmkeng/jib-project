from django.db import models


# Create your models here.
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=50)
