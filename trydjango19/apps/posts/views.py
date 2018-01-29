from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage



# def listing(request):
#     contact_list = Contacts.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page

#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         contacts = paginator.page(paginator.num_pages)

#     return render(request, 'list.html', {'contacts': contacts})


def posts_home(request):
    """ Handles display of all available lists """
    queryset = Posts.objects.all().order_by("-created")
    paginator = Paginator(queryset, 5) # show 5 articles per page
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
