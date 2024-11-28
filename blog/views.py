from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import MyPost

def blog_view(request, **kwargs):
    posts = MyPost.objects.filter(status=1)
    
    if kwargs.get('cat') != None:
        posts = posts.filter(category__name = kwargs["cat"])
        
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs["tag_name"]])   
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {"posts" : posts}
    return render(request, "blog/blog.html", context)

def blog_single(request, pid):
    recent_posts = MyPost.objects.all().order_by("-published_date")[:4]
    posts = MyPost.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    context = {
        "post": post,
        "recent_posts": recent_posts,
        "current_post_id": post.id
               }
    return render(request, "blog/blog-details.html", context)

def blog_category(request, cat):
    posts = MyPost.objects.filter(status=1)
    posts = MyPost.objects.filter(category__name=cat)
    context = {"posts": posts}
    return render(request, "blog/blog.html", context)

def blog_search(request):
    posts = MyPost.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {"posts": posts}
    return render(request, "blog/blog.html", context)

def test(request):
    return render(request, "test.html")
