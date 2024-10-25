from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)