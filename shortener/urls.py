from django.conf.urls import url
from . import views

app_name = 'shortener'

urlpatterns = [
    url(r'^(?P<shortcode>[\w-]+)$', views.get_click_count, name='get_click_count'),
    url(r'^change/(?P<shortcode>[\w-]+)/$', views.change_status, name='change_status'),
]