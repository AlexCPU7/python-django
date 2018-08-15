from django.contrib import admin
from news.models import News, Category, Tag, Comments

# Register your models here.

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')

admin.site.register(Comments, CommentAdmin)
