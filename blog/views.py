from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from blog.models import MyPost, Comment
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse

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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment submited successfully!")
        else:
            messages.error(request, "Your comment did not submit!")
    posts = MyPost.objects.filter(status=1)
    post = get_object_or_404(posts, id=pid)
    if post.login_required == False:
        comments = Comment.objects.filter(post=post.id, applied=True)
        form = CommentForm()
        context = {
            "post": post,
            "comments": comments,
            "form": form,
                }
        return render(request, "blog/blog-details.html", context)
    else:
        return HttpResponseRedirect(reverse("user:login"))

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
