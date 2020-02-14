from django.urls import path
from . import views
"""Так мы импортировали функцию path Django и все views (представления) из приложения blog
первый URL-шаблон:
"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
"""views.post_list — это правильное направление для запроса к твоему веб-сайту по адресу 'http://127.0.0.1:8000/'.
name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его"""
