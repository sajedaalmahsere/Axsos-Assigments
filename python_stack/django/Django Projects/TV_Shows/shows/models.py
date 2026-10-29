from django.db import models
# Create your models here.
class ShowManager(models.Manager):
    def basic_valedator(self, show):
        errors ={}
        title = show.get('title', '').strip()
        network = show.get('network', '').strip()
        comments = show.get('comments', '').strip()
        release_date = show.get('release_date', '').strip()

        if len(title) < 3:
            errors['title'] = "The Title must be at least 3 characters"

        if len(network) < 3:
            errors['network'] = "The Network must be at least 3 characters"

        if len(comments) < 3:
            errors['comments'] = "The Comments must be at least 3 characters"

        if not release_date:
            errors['release_date'] = "The Release Date is required"

        return errors
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    comments = models.TextField()
    release_date = models.DateField()
    user = models.ForeignKey('login.User',related_name= "shows", on_delete=models.CASCADE)
    objects = ShowManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)