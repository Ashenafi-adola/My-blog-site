from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("post", views.post, name="post"),
    path("signin", views.signin, name="signin"),
    path("register", views.register, name="register"),
    path("signout", views.signout, name="signout"),
    path("view-post/<int:pk>", views.view_post, name="viewpost"),
    path("edit/<int:pk>", views.edit_post, name="edit"),
    path("delete/<int:pk>/<int:id>", views.delete_post, name="delete")
]