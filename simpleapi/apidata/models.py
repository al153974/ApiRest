from django.db import models

class Data(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    salary = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    tskills = models.CharField(max_length=6000)
    sskills = models.CharField(max_length=6000)