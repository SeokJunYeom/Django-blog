from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
import handler.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gochiusa/', include('blog.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url = '/static/favicon.ico')),
    url(r'', handler.views.custom_404, name = '404'),
]
