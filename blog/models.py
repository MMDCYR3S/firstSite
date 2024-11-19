from django.db import models

# Create a model for blog.
class MyPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()