from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager 

# Create a model for blog.
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class MyPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to= "blog/", default="blog/default.jpg")
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Any Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return f"{self.id}- {self.title}"
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid":self.id})

class Comment(models.Model):
    post = models.ForeignKey(MyPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    applied = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return self.name
