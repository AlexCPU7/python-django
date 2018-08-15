from django.shortcuts import render
from django.http import HttpResponse

def book_catalog(request):
    return HttpResponse('this catalog')

def book_item(request, id):
    return HttpResponse('product: ' + str(id))
