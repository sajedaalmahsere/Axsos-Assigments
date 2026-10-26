from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, user):
        errors = {}
        first_name = user.get('first_name', '').strip()
        last_name = user.get('last_name', '').strip()
        email = user.get('email', '').strip()
        password = user.get('password', '').strip()
        confirm_password = user.get('confirm_password', '')

        if len(first_name) < 2:
            errors['first_name'] = 'Must be at least 2 characters'

        if not first_name.isalpha():
            errors['first_name'] = 'First name must contain letters only'

        if len(last_name) < 2:
            errors['last_name'] = 'Must be at least 2 characters'

        if not last_name.isalpha():
            errors['last_name'] = 'First name must contain letters only'

        try:
            validate_email(email)
        except:
            errors['email'] = 'Invalid email format'

        if len(password) < 8 :
            errors['password'] = 'Must be at least 8 characters'

        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()