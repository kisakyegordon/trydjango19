from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone, timesince
from django.shortcuts import Http404, render, get_object_or_404, redirect
from .models import Posts
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q



def posts_welcome(request):
    return render(request, "posts/welcome.html")
    

def posts_home(request):
    """ Handles display of all available lists """
    # queryset = Posts.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by("-created")
    queryset = Posts.objects.active().order_by("-created")

    query = request.GET.get("q")
    if query:
        queryset = Posts.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) ).distinct()

    if request.user.is_staff or request.user.is_superuser:
        if query:
            queryset = Posts.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) ).distinct()
        else:
            queryset = Posts.objects.all().order_by("-created")
    paginator = Paginator(queryset, 3) # show 5 articles per page
    page = request.GET.get('page')

    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    context = {
        "lists_all": queryset,
        "lists": lists
    }
    return render(request, "posts/base.html", context)

def posts_create(request):

    if not request.user.is_staff or not request.user.is_superuser:
        return Http404

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Successfully Created")
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm()
    return render(request, "posts/create.html", {'form':form})

def posts_detail(request, id):
    """ Handles single display of an article """
    today = timezone.now().date()
    instance = get_object_or_404(Posts, id=id)
    if instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "title": "Detail is working",
        "instance": instance,
        "today": today,
    }
    return render(request, "posts/post_detail.html", context)

def posts_update(request, id):
    """
    Handles editing an article
    """
    instance = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return redirect("post_home")

    context = {
        "instance": instance,
        "form": form
    }
    return render(request, "posts/create.html", context)


def posts_delete(request, id=None):
    """ Handles deleting an article """
    instance = get_object_or_404(Posts, id=id)
    instance.delete()
    messages.success(request, "Deleted Successfully")
    return redirect("post_home")
