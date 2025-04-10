# Create your views here

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, Category

# home page
def main(request):
    return render(request, 'bloghtml/main.html')

# users
def users(request):
    users_list = User.objects.all()
    return render(request, 'bloghtml/users.html', {'users': users_list})

# blogs
def blogs(request):
    posts = Post.objects.all()
    return render(request, 'bloghtml/blogs.html', {'posts': posts})

# comments
def comments(request):
    all_comments = Comment.objects.all()
    return render(request, 'bloghtml/comments.html', {'comments': all_comments})

# categories
def categories(request):
    categories = Category.objects.all()
    return render(request, 'bloghtml/categories.html', {'categories': categories})

# spicific blogs
def blogdetails(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'bloghtml/blogdetails.html', {'post': post, 'comments': comments})

