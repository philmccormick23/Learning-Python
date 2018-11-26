from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "First name cannot be blank"
        elif not postData['name'].isalpha():
            errors['first_alpha'] = "First name cannot contain numbers"
        if len(postData['alias']) < 2:
            errors['alias'] = "Last name cannot be blank"
        elif not postData['alias'].isalpha():
            errors['last_alpha'] = "Last name cannot contain numbers"
        if len(postData['email']) < 1:
            errors['emails'] = "Emails cannot be blank"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['regex'] = "Not a valid email format"
        if len(postData['password']) < 8:
            errors['password'] = "Password cannot be blank"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Password does not match confirmation"    
        return errors
    
   
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)    
    objects = UserManager()

class Poke(models.Model):
    poker = models.ForeignKey(User, related_name="pokerpokes", on_delete=models.PROTECT)
    poked = models.ForeignKey(User, related_name="pokedpokes", on_delete=models.PROTECT)
    counter = models.IntegerField(blank=False, default=0, null=True)


