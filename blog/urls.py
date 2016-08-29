from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.gochiusa, name = 'gochiusa'),
        url(r'chino/', views.chino, name = 'chino'),
]
