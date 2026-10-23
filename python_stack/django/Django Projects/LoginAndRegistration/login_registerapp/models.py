from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class RegisterManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        first_name = postData.get('first_name', '')
        last_name = postData.get('last_name', '')
        email = postData.get('email', '')
        password = postData.get('password', '')
        confirm_password = postData.get('confirm_password', '')

        if len(first_name) < 2 :
            errors['first_name'] = 'Must be at least 2 characters'

        if not first_name.isalpha():
            errors['first_name'] = 'First name must contain letters only'

        if len(last_name) < 2 :
            errors['last_name'] = 'Must be at least 2 characters'

        if not last_name.isalpha():
            errors['last_name'] = 'Last name must contain letters only'

        # Django checks whether the email is valid.
        try:
            validate_email(email)
        # If the email is invalid, Django catches the error and adds a message to your dictionary.
        except ValidationError:
            errors['email'] = 'Invalid email format'

        if len(password) < 8 :
            errors['password'] = 'Must be at least 8 characters'

        # != checks whether the two passwords are different.
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'
        
        return errors

class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique= True)
    password =models.CharField(max_length=255)
    birthday = models.DateField()
    objects = RegisterManager()

