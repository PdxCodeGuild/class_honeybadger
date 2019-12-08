from django.shortcuts import render
from .models import BlogPost
from django.core.paginator import Paginator
from django.http import HttpResponse

def index(request):
    blog_posts = BlogPost.objects.all()
    paginator = Paginator(blog_posts, 10)
    page = request.GET.get('page', 1)
    blog_posts = paginator.get_page(page)

    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blogapp/index.html', context)


def favorites(request):
    blog_posts = request.user.favorited_blog_posts.all()
    paginator = Paginator(blog_posts, 10)
    page = request.GET.get('page', 1)
    blog_posts = paginator.get_page(page)

    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blogapp/index.html', context)

def favorite_blog_post(request, blog_post_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    user = request.user
    if blog_post in user.favorited_blog_posts.all():
        user.favorited_blog_posts.remove(blog_post)
    else:
        user.favorited_blog_posts.add(blog_post)
    return HttpResponse('ok')
