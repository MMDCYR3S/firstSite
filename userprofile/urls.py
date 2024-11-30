from django.urls import path
from . import views
from userprofile.views import *

app_name = "user"

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.singup_view, name="signup"),
]
