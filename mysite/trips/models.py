import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank = True)
    photo = models.URLField(blank = True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}, {self.created_at}"
    
    def wasPostRecently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)