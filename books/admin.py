from django.contrib import admin
from books.models import Type, Author, Tag, Book

admin.site.register(Type)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Book)
