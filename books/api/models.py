from django.db import models

# Create your models here.


class BooksAPI(models.Model):
    title = models.CharField(max_length=100, default="unknown")
    author = models.CharField(max_length=100, default="unknown")
    description = models.TextField(max_length=200, default="not available")
    img_url = models.CharField(max_length=5000, default="not available")

    class Meta:
        ordering = ["title"]
