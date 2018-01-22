from django.db import models

# Create your models here.

class Posts(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title