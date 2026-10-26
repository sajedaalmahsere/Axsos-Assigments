from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by_id = models.ForeignKey('login.Register', on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Favorite(models.Model):
    book_id = models.ForeignKey(Book, related_name='favorites', on_delete=models.CASCADE)
    user_id = models.ForeignKey('login.Register', on_delete=models.CASCADE, related_name='favorites')
