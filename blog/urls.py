from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
	url(r'^$', views.gochiusa, name = 'gochiusa'),
	url(r'post/$', views.character_post, name = 'character_post'),
	url(r'login/$', login, name = 'login', kwargs = {'template_name' : 'login.html'}),
	url(r'(?P<name>\w+)/$', views.character, name = 'character'),
]
