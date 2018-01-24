from django.conf.urls import url, include
from django.contrib import admin
from .views import ( 
    posts_home,
    posts_create,
    posts_detail,
    posts_update,
    posts_delete,
    )

urlpatterns = [
    url(r'^$', posts_home, name="post_home"),
    url(r'^create$', posts_create),
    url(r'^(?P<id>\d+)/$', posts_detail, name="post_detail"),
    url(r'^update/(?P<id>\d+)/$', posts_update, name="post_update"),
    url(r'^delete$', posts_update),
]