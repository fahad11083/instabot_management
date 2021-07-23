from django.db import models
from django import forms

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user_name}"
