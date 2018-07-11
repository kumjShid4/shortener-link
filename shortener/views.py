from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from analytics.models import ClickCount
from .forms import URLForm
from .models import URL
from .utils import validate_url

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
                #if user is logged in
                if request.user.id:
                    obj.user = request.user
                obj.save()
                ClickCount.objects.create_event(obj)
                return redirect('/')
            else:
                valid = False
    urls = URL.objects.all().filter(status__exact='public').order_by('-timestamp')
    paginator = Paginator(urls, 10)
    page = request.GET.get('page')
    urls_display = paginator.get_page(page)
    return render(request, 'shortener/index.html', {'form': form, 'valid': valid, 'urls_display': urls_display})

def redirect_url(request, shortcode):
    try:
        url = get_object_or_404(URL, short_code=shortcode)
    except:
        return render(request, 'shortener/404.html')
    else:
        ClickCount.objects.create_event(url)
        trueurl = url.url
        if trueurl.find('http') == -1:
            trueurl = 'https://' + trueurl
        return redirect(trueurl)

def get_click_count(request, shortcode):
    if request.method == 'GET':
        try:
            url = get_object_or_404(URL, short_code=shortcode)
        except:
            return JsonResponse({'clickcount': -1})
        else:        
            clickcount = ClickCount.objects.create_event(url)
            return JsonResponse({'clickcount': clickcount})
    
def error404(request):
    return render(request, 'shortener/404.html')

def error500(request):
    return render(request, 'shortener/500.html')

@login_required
def change_status(request, shortcode):
    try:
        url = get_object_or_404(URL, short_code=shortcode)
    except:
        return JsonResponse({'status': 'undefined'})
    else:
        if request.user.is_authenticated:
            if url.status == 'public':
                url.status = 'private'
            else:
                url.status = 'public'
            url.save()
            return JsonResponse({'status': url.status})
        else:
            return JsonResponse({'status': url.status})