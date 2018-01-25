from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from .forms import PostForm

def posts_home(request):
    """ Handles display of all available lists """
    queryset = Posts.objects.all()
    context = {
        "lists_all": queryset
    }
    return render(request, "posts/index.html", context)

def posts_create(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Successfully Created")
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm()
    return render(request, "posts/create.html", {'form':form})

def posts_detail(request, id):
    """
    Handles single display of an article
    """
    instance = get_object_or_404(Posts, id=id)
    context = {
        "title": "Detail is working",
        "instance": instance
    }
    return render(request, "posts/post_detail.html", context)

def posts_update(request, id):
    """
    Handles editing an article
    """
    instance = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, instance=instance)
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
    """
    Handles deleting an article
    """
    instance = get_object_or_404(Posts, id=id)
    instance.delete()
    messages.success(request, "Deleted Successfully")
    return redirect("post_home")

