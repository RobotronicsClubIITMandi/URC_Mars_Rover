from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={})

def team(request):
    return render(request, 'team.html', context={})

def blog(req):
    return render(req, 'blog.html', context={})

def gallery(req):
    return render(req, 'gallery.html', context={})

def contact(req):
    return render(req, 'contact.html', context={})