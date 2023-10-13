from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=100)  # 국가 필드 추가
    location = models.CharField(max_length=100)  # 지역 필드 추가

    def __str__(self):
        return self.name