from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.contrib import messages
from website.models import Contact
from website.forms import *

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "You ticket submited successfully!")
        else:
            messages.add_message(request,messages.ERROR, "Error: Your ticket didn't submit!")
    form = ContactForm()
    return render(request, 'website/contact.html', {"form": form})

def subscribe_view(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("All Done!")
        else:
            return HttpResponse("Error: Not Valid!")
    form = ContactForm()
    return render(request, 'test.html', {'form': form})