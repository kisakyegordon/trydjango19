from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import home_index

urlpatterns = [
    url(r'^', home_index),
]
