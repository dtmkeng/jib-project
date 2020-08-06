from django.db import models

# Create your models here
# 1. Migrate

class Worker(models.Model): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    is_available = models.BooleanField()
    primary_phone = models.CharField(max_length=10)
    secondary_phone = models.CharField(max_length=10)
    address = models.TextField()