from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('home', ViewArticles),
    path('post', PostArticles.as_view())
]
