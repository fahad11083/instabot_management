from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user_name}"


class Order(models.Model):
    like_service_purchased = models.BooleanField(default=False)
    comment_service_purchased = models.BooleanField(default=False)
    follower_service_purchased = models.BooleanField(default=False)
    picture_link = models.CharField(max_length=1000)
    number_of_users = models.IntegerField(default=0)
    comment_message = models.CharField(max_length=500)
    amount_of_likes = models.IntegerField(default=0)
    number_of_followers = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    account_link = models.CharField(null=True, max_length=1000)
