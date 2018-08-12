from django.shortcuts import render
from django.http import HttpResponse
from news.models import News

# Create your views here.

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {
        "news": news
    })

def k(request):
    return HttpResponse('k')

def j(request):
    return HttpResponse('j')