from django.db import models
import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)