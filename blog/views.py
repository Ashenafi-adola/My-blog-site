from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, Comment

def register(request):

    context = {

    }
    return render(request, 'blog/signin_signup.html',context)

def signin(request):

    context = {

    }
    return render(request, 'blog/signin_signup.html',context)

def signout(request):

    pass

def home(request):
    posts = Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request, 'blog/home.html',context)

def post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form":form,
    }
    return render(request, 'blog/post.html',context)