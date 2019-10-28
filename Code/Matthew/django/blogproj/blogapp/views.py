from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, BlogPostCategory

def index(request):
    # return HttpResponse('happy monday :)')
    
    blog_posts = BlogPost.objects.order_by('date_published')
    blog_post_categories = BlogPostCategory.objects.order_by('name')
    context = {
        'blog_posts': blog_posts,
        'blog_post_categories': blog_post_categories
    }
    return render(request, 'blogapp/index.html', context)

def detail(request, blog_post_slug):
    # return HttpResponse(f'You are looking at the blog post detail page for blog post id {blog_post_id}')
    single_post = BlogPost.objects.get(slug=blog_post_slug)
    context = {
        'single_post': single_post
    }
    return render(request, 'blogapp/detail.html', context)
    
def create_blogpost(request):
    # print('='*100)
    print(request.POST)
    title_shark = request.POST['title_llama']
    author_shark = request.POST['author_llama']
    slug_shark = request.POST['slug_llama']
    body_shark = request.POST['body_llama']
    category_id_shark = request.POST['category_id_llama']
    
    # blog_post_category_shark = BlogPostCategory.objects.get(id=category_id_shark)
    # blog_post = BlogPost(title=title_shark,
    #                      author=author_shark,
    #                      slug=slug_shark,
    #                      body=body_shark,
    #                      category=blog_post_category_shark)
    
    blog_post = BlogPost(title=title_shark,
                         author=author_shark,
                         slug=slug_shark,
                         body=body_shark,
                         category_id=category_id_shark)
    blog_post.save()
    return HttpResponseRedirect(reverse('blogapp:index'))