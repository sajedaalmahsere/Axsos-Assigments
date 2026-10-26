from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    user_id = models.ForeignKey('login.User',related_name= "messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey('login.User',related_name= "comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)