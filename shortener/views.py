from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import URLForm
from .models import URL
from .utils import validate_url
from analytics.models import ClickCount
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    valid = True
    form = URLForm()
    if request.method == "POST":
        try:
            validate_url(request.POST['url'])
        except ValidationError:
            valid = False
        else:
            valid = True
            form = URLForm(request.POST)
            if form.is_valid():
                obj = URL()
                obj.url = form.cleaned_data['url']
                obj.save()
                ClickCount.objects.create_event(obj)
                return redirect('/')
            else:
                valid = False
    urls = URL.objects.all()
    paginator = Paginator(urls, 10)
    page = request.GET.get('page')
    urls_display = paginator.get_page(page)
    return render(request, 'shortener/index.html', {'urls': urls, 'form': form, 'valid': valid, 'urls_display': urls_display})


def redirect_url(request, shortcode):
    url = get_object_or_404(URL, short_code=shortcode)
    ClickCount.objects.create_event(url)
    return redirect(url.url)
