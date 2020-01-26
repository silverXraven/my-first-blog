from django.urls import path
from . import views
"""Так мы импортировали функцию path Django и все views (представления) из приложения blog
первый URL-шаблон:
"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
"""views.post_list — это правильное направление для запроса к твоему веб-сайту по адресу 'http://127.0.0.1:8000/'.
name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его"""
