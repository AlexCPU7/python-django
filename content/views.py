from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def type(request):
    return HttpResponse('type')

def form(request):
    return render(request, 'form.html')

def form_res(request):
    if request.POST:
        return HttpResponse('Request is POST')
    else:
        return HttpResponse('Request is GET')

