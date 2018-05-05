from django.db import models



class register(models.Model):
    res_username = models.CharField(max_length=30, null=True)
    res_password = models.CharField(max_length=30, null=True)
    res_email = models.CharField(max_length=30, null=True)