from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
# Create your views here.

def posts_home(request):
    queryset = Posts.objects.all()
    context = {
        "lists_all": queryset
    }
    return render(request, "posts/index.html", context)
    # return HttpResponse("<h1> Hello </h1>")

def posts_create(request):
    # return HttpResponse("<h1> Create </h1>")
    context = {
        "title": "Create is working"
    }
    return render(request, "posts/index.html", context)

def posts_detail(request):
    # return HttpResponse("<h1> Detail</h1>")
    context = {
        "title": "Detail is working"
    }
    return render( request, "posts/index.html", context)

def posts_update(request):
    return HttpResponse("<h1> Update </h1>")

def posts_delete(request):
    return HttpResponse("<h1> Delete </h1>")
