from django.shortcuts import render, redirect, get_object_or_404
from info.models import Content
from news.models import News, Comments


def index(request):
    return render(request, 'info/index.html')


def project(request):
    info = get_object_or_404(Content, id=1)
    return render(request, 'info/project.html', {
        'info': info
    })
