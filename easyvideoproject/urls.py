"""easyvideoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from video import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^video/(?P<vid>\d+)/$', views.videoDetail, name='videoDetail'),
    url(r'^history/$', views.viewHistory, name="viewHistory"),
    url(r'^cate/(?P<cateid>\d+)/$', views.videoCate, name='videoCate'),
    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^like/$', views.like, name='like'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }, name='media'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }, name='static'),
    url(r'^check_code', views.check_code, name='check_code'),
]
