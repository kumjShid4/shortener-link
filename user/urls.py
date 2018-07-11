from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', LoginView.as_view(template_name='user/login.html',
                                       redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^tracking/$', views.tracking, name='tracking'),
    url(r'^delete/(?P<shortcode>[\w-]+)/$', views.delete_url, name='delete_url'),
]
