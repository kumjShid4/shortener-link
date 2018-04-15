from django.shortcuts import render, get_object_or_404, redirect
from .forms import URLForm
from .models import URL
# Create your views here.


def index(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            return redirect('shortener:index')
    else:
        form = URLForm()
    urls = URL.objects.all()
    form.fields['url'].widget.attrs = {"class": "form-control", 'placeholder':'Your original url here.'}
    return render(request, 'shortener/index.html', {'urls': urls, 'form': form})


def shortener(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            return redirect('blog:index')
