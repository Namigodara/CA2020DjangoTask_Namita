from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.title}"
