from django.urls import path
from . import views

urlpatterns = [
    path('dog/', views.dog, name='dog'),
    path('add-dog/', views.add_dog, name='add-dog'),
]
