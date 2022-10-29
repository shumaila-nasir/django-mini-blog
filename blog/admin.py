from django.contrib import admin
from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

admin.site.register(Post)
