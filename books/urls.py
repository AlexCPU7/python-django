from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_catalog, name='catalog'),
    path('book/<int:id>', views.book_item, name='product'),
    path('add_book/', views.add_book, name='add_book')
]