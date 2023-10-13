from django.db import models
from django.conf import settings
# Create your models here.

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name