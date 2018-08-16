from django.shortcuts import render, get_object_or_404, redirect
from .models import Book


def book_catalog(request):
    books = Book.objects.all()
    return render(request, 'books/book_catalog.html', {
        'books': books
    })


def book_item(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_item.html', {
        'book': book
    })
