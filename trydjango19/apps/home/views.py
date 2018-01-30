from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import Http404, render, get_object_or_404, redirect

def home_index(request):
    return render(request, "home/home.html")
