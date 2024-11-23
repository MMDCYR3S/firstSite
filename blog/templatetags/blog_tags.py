from django import template
from blog.models import MyPost, Category

register = template.Library()

@register.simple_tag(name="totalPosts")
def num_function():
    posts = MyPost.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="posts")
def num_function():
    posts = MyPost.objects.filter(status=1)
    return posts

@register.filter
def snippets(text, arg=20):
    return text[:arg] + "..."

@register.inclusion_tag("blog/blog-recent.html")
def latestposts(arg=3):
    posts = MyPost.objects.filter(status=1,).order_by("-published_date")[:arg]
    return {"posts": posts}

@register.inclusion_tag("blog/blog-category.html")
def postcategories():
    posts = MyPost.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories" : cat_dict}
        
