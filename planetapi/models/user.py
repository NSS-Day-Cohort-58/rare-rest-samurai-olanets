from django.db import models
from django.contrib.auth.models import User

class User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    img = models.URLField(max_length=300, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(blank = True)