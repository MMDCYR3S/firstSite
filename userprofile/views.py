from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Creating views for users' login, signup and logout.
def login_view(request):
    """ Create function for login"""
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                return redirect("/")
            messages.error(request,"The username or password is wrong!")
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "profile/login.html", context)
    else:
        return redirect("/")

@login_required(login_url="./login")
def logout_view(request):
    logout(request)
    return redirect("/")

def singup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("./login")
            messages.error(request,"The password and confirm password are not the same!")
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "profile/signup.html", context)
    else:
        return redirect("/")
