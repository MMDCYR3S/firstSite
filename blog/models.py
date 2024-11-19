from django.db import models

# Create a model for blog.
class MyPost(models.Model):
    # author
    # image
    title = models.CharField(max_length=200)
    content = models.TextField()
    # tag
    # category
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Any Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return f"{self.id}- {self.title}"
    
    