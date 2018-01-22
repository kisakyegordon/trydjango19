from django.contrib import admin

# Register your models here.
from .models import Posts

class PostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Posts

admin.site.register(Posts, PostModelAdmin)
