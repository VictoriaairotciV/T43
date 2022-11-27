from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('hobbies', views.hobbies),
]
