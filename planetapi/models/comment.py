from django.db import models

class Comment(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment")
    content = models.CharField(max_length=1000)

    @property
    def author_name(self):
        return f'{self.author.full_name}'