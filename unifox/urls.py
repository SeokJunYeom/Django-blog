from django.conf.urls import include, url
from django.contrib import admin
import handler.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gochiusa/', include('blog.urls')),
    url(r'', handler.views.custom_404, name = '404'),
]
