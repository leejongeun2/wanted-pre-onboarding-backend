from django.db import models
from django.conf import settings
# Create your models here.

class Applicant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    
    def __str__(self):
        return self.name