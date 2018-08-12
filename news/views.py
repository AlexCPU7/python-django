from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from news.models import News

# Create your views here.

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {
        "news": news
    })

def new(request, pk):
    new = get_object_or_404(News, id=pk)
    return render(request, 'news/new.html', {
        'new': new
    })

def k(request):
    return HttpResponse('k')

def j(request):
    return HttpResponse('j')