
    # Title
    # Content
    # Category
    # Publication date (current date)
    # Header Image URL (optional)

from django.db import models

class Post(models.model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=512)
    category = models.ForeignKey("Category")
    publication_date = models.DateField()
    image = models.CharField(max_length=512)
