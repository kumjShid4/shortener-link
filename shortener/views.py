from django.shortcuts import render, get_object_or_404, redirect
from .forms import URLForm
from .models import URL
# Create your views here.

def index(request):
    if request.method == "POST":
        print(request.method)
        form = URLForm(request.POST)
        print(form.errors)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            print(url)
            return redirect('blog:index')
    else:
        form = URLForm()
    urls = URL.objects.all()
    return render(request, 'shortener/index.html', {'urls': urls})

def shortener(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            return redirect('blog:index')
