from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('search', views.search, name = "search"),
    path('<str:slug>/', views.movie_detail, name = "movie"),
]
