from django.shortcuts import render

def blog_view(request):
    return render(request, "blog/blog.html")
def blog_single(request):
    context = {"title": "I don't have a fucking clue!", "content": "What do you want me to say? Fuck Off!", "author": "Mamad CYR3S"}
    return render(request, "blog/blog-details.html", context)