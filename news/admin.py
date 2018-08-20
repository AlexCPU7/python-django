from django.contrib import admin
from news.models import News, Category, Tag, Comments

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'text', 'created', 'moderation')


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments, CommentAdmin)
