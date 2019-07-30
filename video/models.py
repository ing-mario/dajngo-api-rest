from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50)
    created_at = models.DateField(auto_now=True)