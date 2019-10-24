from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogPost, BlogPostType

# BlogPost.objects.order_by('title').filter(type_id=1)[:5]
def index(request):
    blog_posts = BlogPost.objects.order_by('date_created')
    # blog_posts_processed = []
    # for blog_post in blog_posts:
    #     blog_posts_processed.append({
    #         'title': blog_post.title,
    # 
    #     })
    
    context = {
        'title': 'hello world! welcome to my blog :)',
        'blog_posts': blog_posts
    }
    return render(request, 'blogapp/index.html', context)

def detail(request, blog_post_id):
    # use the orm to find the blog post with the given id
    blog_post = BlogPost.objects.get(id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    # return HttpResponse('this is a blog post detail page for the blog post with id ' + str(blog_post_id))
    return render(request, 'blogapp/detail.html', context)