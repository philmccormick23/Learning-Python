from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "First name is too short"
        elif not postData['name'].isalpha():
            errors["first_alpha"] = "No numbers allowed"
        if len(postData['alias']) < 2:
            errors["alias"] = "Last name is too short"
        elif not postData['alias'].isalpha():
            errors["last_alpha"] = "No numbers allowed"
        if len(postData['email']) < 1:
            errors["email"] = "Email is too short"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email_valid"] = "Email wrong format"
        if len(postData['password']) < 8:
            errors["password"] = "Password is too short"
        if postData['password'] != postData['confirm']:
            errors["confirmation"] = "Your emails don't match"
        return errors



class User(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="user_book", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review = models.CharField(max_length=1000)
    rating = models.IntegerField()
    user = models.ForeignKey (User, related_name="user_review", on_delete=models.PROTECT)
    book = models.ForeignKey (Book, related_name="book_review", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
