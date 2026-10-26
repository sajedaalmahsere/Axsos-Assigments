from django.db import models
from django.core.validators import validate_email
# Create your models here.
class RegisterManager(models.Manager):
    def basic_validator(self , postData):
        errors = {}
        first_name = postData.get('first_name', '').strip()
        last_name = postData.get('last_name', '').strip()
        email = postData.get('email', '').strip()
        password = postData.get('password', '').strip()
        confirm_password = postData.get('confirm_password', '').strip()

        if len(first_name)< 2:
            errors['first_name'] = 'Must be at least 2 characters'

        if len(last_name)< 2:
            errors['last_name'] = 'Must be at least 2 characters'

        try:
            validate_email(email)
        except:
            errors['email'] = 'Invalid email format'

        if len(password) < 8 :
            errors['password'] = 'Must be at least 8 characters'

        if password != confirm_password :
            errors['confirm_password'] = 'Passwords do not match'

        return errors

class Register(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegisterManager()




