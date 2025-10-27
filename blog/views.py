from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            return redirect('signin')
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'blog/signin_signup.html',context)

def signin(request):
    page = 'signin'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('home')

    context = {
        'page':page,
    }
    return render(request, 'blog/signin_signup.html',context)

def signout(request):
    logout(request)
    return redirect('signin')


def home(request):
    posts = Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request, 'blog/home.html',context)


@login_required(login_url='signin')
def post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    context = {
        "form":form,
    }
    return render(request, 'blog/post.html',context)

def view_post(request,pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post).order_by('-commented_at')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(f'/view-post/{pk}')
    context = {
        'post':post,
        'form':form,
        'comments':comments,
    }
    return render(request, 'blog/post-view.html', context)

def edit_post(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/view-post/{pk}')
    context = {
        'form':form,

    }
    return render(request, 'blog/post.html', context)

def delete_post(request,pk,id):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete.html', {})

def delete_post(request,pk,id):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect(f'/view-post/{id}')

    return render(request, 'blog/delete.html', {})