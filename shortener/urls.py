from django.conf.urls import url
from . import views

app_name = 'shortener'

urlpatterns = [
    url(r'^(?P<shortcode>[\w-]+)/$', views.getClickCount, name='getClickCount'),
]