from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm

def register(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'blog/signin_signup.html',context)

def signin(request):
    page = 'signin'
    context = {
        'page':page,
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