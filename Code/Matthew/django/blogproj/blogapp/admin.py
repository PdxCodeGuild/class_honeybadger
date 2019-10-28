from django.contrib import admin

from .models import BlogPost, BlogPostCategory

admin.site.register(BlogPost)
admin.site.register(BlogPostCategory)
