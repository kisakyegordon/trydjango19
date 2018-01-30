from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import ( 
    posts_home,
    posts_create,
    posts_detail,
    posts_update,
    posts_delete,
    posts_welcome,
    )

urlpatterns = [
    # url(r'^$', posts_welcome),
    url(r'^$', posts_home, name="post_home"),
    url(r'^create$', posts_create),
    url(r'^(?P<id>\d+)/$', posts_detail, name="post_detail"),
    url(r'^(?P<id>\d+)/update$', posts_update, name="post_update"),
    url(r'^(?P<id>\d+)/delete$', posts_delete, name="post_delete"),
]
