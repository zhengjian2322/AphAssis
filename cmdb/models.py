
from django.db import models
from django.contrib import admin

class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)