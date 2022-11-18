from django.db import models

class Tag(models.Model):
    label = models.ManyToManyField("Post", through="PostTag", related_name="tag")