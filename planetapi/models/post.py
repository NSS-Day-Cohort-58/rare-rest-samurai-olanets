
from django.db import models
from django.contrib.auth.models import User
from .category import Category

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=512)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    date = models.DateField()
    image = models.CharField(max_length=512)
