from django.db import models

class Link(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
