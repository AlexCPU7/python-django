from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from . import forms


def book_catalog(request):
    books = Book.objects.all()
    return render(request, 'books/book_catalog.html', {
        'books': books,
    })


def book_item(request, id):
    book = get_object_or_404(Book, id=id)
    language = book.array_language[book.language - 1][1]
    return render(request, 'books/book_item.html', {
        'book': book,
        'language': language
    })


def add_book(request):
    form_book = forms.BookForm
    form = forms.BookForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        form = form.save()
        return redirect('/catalog/book/')
    return render(request, 'books/add_book.html', {
        'title': 'Добавить книгу',
        'form_book': form_book
    })