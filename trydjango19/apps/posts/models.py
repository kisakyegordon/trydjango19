from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Posts(models.Model):

    title = models.CharField(max_length=120)
    image = models.FileField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

def pre_save_slug(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    unique_slug = slug
    num = 1
    while Posts.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    instance.slug = unique_slug
    # return unique_slug

pre_save.connect(pre_save_slug, sender=Posts)
