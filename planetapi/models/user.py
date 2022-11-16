from django.db import models
from django.contrib.auth.models import User

class User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    profile_img_url = models.URLField(max_length=300, blank=True)
    created_on = models.DateField.auto_now()
    active = models.BooleanField()