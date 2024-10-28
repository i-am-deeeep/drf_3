from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=30)
    blogpost=models.CharField(max_length=4000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
