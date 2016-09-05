from django.conf.urls import include, url, handler404
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gochiusa/', include('blog.urls')),
]

handler404 = 'handler.views.custom_404'
