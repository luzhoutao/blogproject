from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 200, blank = True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    auth = models.ForeignKey(User)

    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('iblog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views = self.views+1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time', 'title']
