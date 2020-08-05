from django.db import models

class MyUser(models.Model):
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)