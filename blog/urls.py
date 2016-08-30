from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.gochiusa, name = 'gochiusa'),
        url(r'(?P<name>\w+)/$', views.character, name = 'character'),
]
