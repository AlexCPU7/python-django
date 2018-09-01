from django.forms import ModelForm
from .models import Book, Author, Type


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'type_id', 'author', 'image', 'file', 'link', 'desc', 'language', 'pages', 'year', 'tags']