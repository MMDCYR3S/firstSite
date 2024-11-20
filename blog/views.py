from django.shortcuts import render, get_object_or_404
from blog.models import MyPost

def blog_view(request):
    posts = MyPost.objects.filter(status=1)
    context = {"posts" : posts}
    return render(request, "blog/blog.html", context)

def blog_single(request, pid):
    posts = MyPost.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    context = {"post": post}
    return render(request, "blog/blog-details.html", context)

def test(request, pid):
    #post = MyPost.objects.get(id=pid)
    post = get_object_or_404(MyPost,pk=pid)
    context = {"post": post}
    return render(request, "test.html", context)