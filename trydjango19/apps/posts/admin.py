from django.contrib import admin

# Register your models here.
from .models import Posts

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "updated"]
    list_filter = ["created", "updated"]
    list_display_links = ["created"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Posts

admin.site.register(Posts, PostModelAdmin)
