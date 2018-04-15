from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import URLForm
from .models import URL
from analytics.models import ClickCount

# Create your views here.


def index(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            ClickCount.objects.create_event(url)
            return redirect('shortener:index')
    else:
        form = URLForm()
    urls = URL.objects.all()
    return render(request, 'shortener/index.html', {'urls': urls, 'form': form})


def redirect_url(request, shortcode):
    url = get_object_or_404(URL, short_code=shortcode)
    ClickCount.objects.create_event(url)
    return redirect(url.url)