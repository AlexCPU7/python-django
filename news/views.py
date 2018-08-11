from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def k(request):
    return HttpResponse('k')

def j(request):
    return HttpResponse('j')