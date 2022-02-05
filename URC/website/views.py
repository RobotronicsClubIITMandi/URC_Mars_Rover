from multiprocessing import context
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Comments
from . forms import CommentForm


def index(request):
    return render(request, 'index.html', context={})

def team(request):
    return render(request, 'team.html', context={})

def blog(req):
    all_blogs = Blog.objects.all()
    context = {'all_blogs':all_blogs}
    return render(req, 'blog.html', context=context)

def blog_details(req, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    comments = blog.comments_set.all()
    all_blogs = Blog.objects.all()
    
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            author = req.user
            comment = Comments(author=author, blog = blog, text = form.cleaned_data['comment'])
            comment.save()

    form = CommentForm()
    context = {'blog': blog, 'all_blogs': all_blogs, 'comments':comments, 'form':form}
    return render(req, 'blog-details.html', context=context)

def gallery(req):
    return render(req, 'gallery.html', context={})

def contact(req):
    return render(req, 'contact.html', context={})