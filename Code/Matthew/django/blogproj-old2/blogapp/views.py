from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import BlogPost, BlogPostType

def index(request):
    blog_posts = BlogPost.objects.order_by('-published_date')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blogapp/index.html', context)

def detail(request, blog_post_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blogapp/detail.html', context)



def create_blogpost(request):
    print(request.POST)
    blogpost_title = request.POST['blogpost_title']
    blogpost_body = request.POST['blogpost_body']
    blogpost_type_id = request.POST['blogpost_type_id']
    
    blogpost = BlogPost(title = blogpost_title,
                        body = blogpost_body,
                        type_id = blogpost_type_id)
                        
    # blogpost_type = BlogPostType.objects.get(id=blogpost_id)
    # blogpost = BlogPost(title = blogpost_title,
    #                     body = blogpost_body,
    #                     type = blogpost_type)
    blogpost.save()
    
    return HttpResponseRedirect(reverse('blogapp:index'))


def new(request):
    
    blogpost_types = BlogPostType.objects.order_by('name')
    context = {
        'blogpost_types': blogpost_types
    }
    return render(request, 'blogapp/new.html', context)