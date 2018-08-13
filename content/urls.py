from django.urls import path
from . import views

urlpatterns = [
    path('type/', views.type),
    path('form/', views.form),
    path('form-res/', views.form_res)
]
