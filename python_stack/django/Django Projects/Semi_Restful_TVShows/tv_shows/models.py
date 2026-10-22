from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, movie):
        errors ={}
        title = movie.get('title', '')
        network = movie.get('network', '')
        description =  movie.get('description', '')

        if len(title) < 2:
            errors['title'] = "Blog name should be at least 2 characters."

        if len(network) < 3:
            errors['network'] = "Blog description should be at least 3 characters."

        if len(description) < 10:
            errors['description'] = "Blog description should be at least 10 characters."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    
