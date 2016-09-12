from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.gochiusa, name = 'gochiusa'),
        url(r'post$', views.character_post, name = 'character_post'),
        url(r'(?P<name>\w+)/$', views.character, name = 'character'),
]
