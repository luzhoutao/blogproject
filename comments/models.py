from django.db import models
from iblog.models import Post
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-created_time', 'name']
