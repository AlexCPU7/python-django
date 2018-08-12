from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='list_news'),
    path('<int:pk>', views.new, name='new'),
    path('k/', views.k),
    path('j/', views.j)
]