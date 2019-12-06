from django.conf import settings #открывают доступ к коду из других файлов
from django.db import models #открывают доступ к коду из других файлов
from django.utils import timezone #открывают доступ к коду из других файлов

# class — это специальное ключевое слово для определения объектов.
# Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя). Всегда начинай имена классов с прописной буквы.
# models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.
class Post(models.Model): #эта строка определяет нашу модель (объект)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ссылка на другую модель
    title = models.CharField(max_length=200) #— так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField() #так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста, верно?
    created_date = models.DateTimeField(default=timezone.now) #дата и время.
    published_date = models.DateTimeField(blank=True, null=True)#дата и время.

    def publish(self): #метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #получим текст (строку) с заголовком записи
        return self.title
