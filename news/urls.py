from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='list_news'),
    path('k/', views.k),
    path('j/', views.j)
]