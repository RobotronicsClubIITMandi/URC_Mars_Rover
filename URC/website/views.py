from multiprocessing import context
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog


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
    all_blogs = Blog.objects.all()
    context = {'blog': blog, 'all_blogs': all_blogs}
    return render(req, 'blog-details.html', context=context)

def gallery(req):
    return render(req, 'gallery.html', context={})

def contact(req):
    return render(req, 'contact.html', context={})