from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    bio = models.CharField(max_length=50)
    img = models.URLField(max_length=300, blank=True)
    active = models.BooleanField()


    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'