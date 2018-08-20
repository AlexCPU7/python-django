from django.contrib import admin
from books.models import Type, Author, Tag, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_id', 'year', 'pages', 'language', 'create_dt')
    list_editable = ['type_id']
    search_fields = ['title']  #tags__title
    list_filter = ('type_id', 'year', 'language', 'tags',  'create_dt')


admin.site.register(Type)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Book, BookAdmin)
