from django.urls import path
from . import views

urlpatterns = [
    path('k/', views.k),
    path('j/', views.j)
]