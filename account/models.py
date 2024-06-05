from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='user_articles', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
class Article(models.Model):
    author = models.ForeignKey(User, related_name='user_articles')