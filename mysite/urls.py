"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    Строки, расположенные между тройными кавычками (''' , называются docstrings — ты можешь добавить их в начале файла, класса или метода для описания их функциональности. Python будет их игнорировать при запуске приложения.
    любому URL-адресу, начинающемуся с admin/, Django будет находить соответствующее view (представление). В этом случае мы охватываем большое количество различных URL-адресов, которые явно не прописаны в этом маленьком файле — так он становится более аккуратным и удобочитаемым.
    Django теперь будет перенаправлять все запросы 'http://127.0.0.1:8000/' к blog.urls и искать там дальнейшие инструкции.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
]
