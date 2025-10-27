from django.urls import path
from . import views
urlpatterns = [
    path("home", views.home, name="home"),
    path("post", views.post, name="post"),
    path("signin", views.signin, name="signin"),
    path("register", views.register, name="register"),
    path("signout", views.signout, name="signout")
]