# from django.contrib import admin
# импорт include позволит использовать адреса, включенные в приложения
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
