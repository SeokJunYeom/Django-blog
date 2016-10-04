from django.conf import settings
from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.static import serve
from django.contrib.auth.views import login
from . import views

urlpatterns = [
	url(r'^$', views.gochiusa, name = 'gochiusa'),
        url(r'^favicon\.ico$', RedirectView.as_view(url = '/static/favicon.ico')),
	url(r'post/$', views.character_post, name = 'character_post'),
	url(r'login/$', login, name = 'login', kwargs = {'template_name' : 'login.html'}),
	url(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	url(r'(?P<name>\w+)/$', views.character, name = 'character'),
]
