from django.db import models
from django.urls import reverse

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def get_absolute_url(self):
        return reverse('homepage')

    def __str__(self):
        return self.name
