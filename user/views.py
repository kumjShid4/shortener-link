from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from shortener.views import index
from shortener.models import URL
from .forms import UserForm


def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    if not request.user.is_authenticated:
        if request.method != 'POST':
            form = UserForm()
        else:
            form = UserForm(data=request.POST)
            if form.is_valid():
                newUser = form.save()
                authenticated_user = authenticate(username=newUser.username, password=request.POST.get('password1'))
                login(request, authenticated_user)
                return redirect('/')
        return render(request, 'user/signup.html', {'form': form})
    else:   
        return redirect('/')

def login_view(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return login(request, 'user/login.html')

@login_required
def tracking(request):
    urls = URL.objects.filter(user__exact=request.user).order_by('-timestamp')
    paginator = Paginator(urls, 10)
    page = request.GET.get('page')
    urls_display = paginator.get_page(page)
    return render(request, 'user/tracking.html', {'urls_display': urls_display})

@login_required
def delete_url(request, shortcode):
    try:
        url = get_object_or_404(URL, short_code=shortcode, user=request.user)
    except:
        return render(request, 'shortener/404.html')
    else:
        url.delete()
        return redirect('user:tracking')