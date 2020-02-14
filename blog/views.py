from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


#Точка перед models означает текущую директорию или текущее приложение. Поскольку views.py и models.py находятся в одной директории, мы можем использовать точку . и имя файла (без расширения .py). Затем мы импортируем модель (Post).
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#Нам осталось передать QuerySet posts в шаблон
    return render(request, 'blog/post_list.html',{'posts': posts})#это место, куда мы можем добавить что-нибудь для использования в шаблоне. )
#Как ты можешь заметить, мы создали функцию (def) с именем post_list, которая принимает request в качестве аргумента и возвращает (return) результат работы функции render, которая уже соберёт наш шаблон страницы blog/post_list.html.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
