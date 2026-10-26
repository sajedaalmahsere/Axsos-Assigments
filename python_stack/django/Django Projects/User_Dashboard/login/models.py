from django.db import models
from django.core.validators import validate_email

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email = postData.get('email', '').strip()
        first_name = postData.get('first_name', '').strip()
        last_name = postData.get('last_name', '').strip()
        password = postData.get('password', '').strip()
        confirm_password = postData.get('confirm_password', '').strip()

        try:
            validate_email(email)
        except:
            errors['email'] = "Invalid email"

        if len(first_name)< 2:
            errors['first_name'] = "Invalid first name it should be at least 2 characters"

        if len(last_name)< 2:
            errors['last_name'] = "Invalid last name it should be at least 2 characters"

        if len(password) < 8:
            errors['password'] = "Invalid password it should be at least 8 characters"

        if password != confirm_password:
            errors['confirm_password'] = "Passwords do not match"

class User(models.Model):
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_level = models.IntegerField(default=1)


