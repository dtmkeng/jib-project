from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    is_available = models.BooleanField()
    primary_phone = models.CharField(max_length=10)
    secondary_phone = models.CharField(max_length=10)
    address = models.TextField()
    image_proflie = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
