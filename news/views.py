from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from news.models import News, Comments
from news.forms import CommentForm


def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {
        "news": news
    })


def new(request, pk):
    new = get_object_or_404(News, id=pk)
    comments = Comments.objects.filter(new=pk, moderation=True)
    if request.POST:
        comm_form = CommentForm(request.POST)
        if comm_form.is_valid():
            comm_form = comm_form.save(commit=False)
            comm_form.user = request.user
            comm_form.new = new
            comm_form.save()
            return redirect('/news/' + str(pk))
    else:
        comm_form = CommentForm()
    return render(request, 'news/new.html', {
        'new': new,
        'comments': comments,
        'comm_form': comm_form
    })


def k(request):
    return HttpResponse('k')


def j(request):
    return HttpResponse('j')