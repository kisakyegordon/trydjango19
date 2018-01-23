from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', "trydjango19.apps.posts.views.posts_home"),
    url(r'^create$', "trydjango19.apps.posts.views.posts_create"),
    url(r'^detail$', "trydjango19.apps.posts.views.posts_detail"),
    url(r'^update$', "trydjango19.apps.posts.views.posts_update"),
    url(r'^delete$', "trydjango19.apps.posts.views.posts_delete"),
]