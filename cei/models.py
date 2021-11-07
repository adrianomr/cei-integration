from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.TextField(max_length=1000)