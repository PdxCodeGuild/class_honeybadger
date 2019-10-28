from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {
        # 'title': 'hello world! welcome to my blog :)'
    }
    return render(request, 'blogapp/index.html')

def about(request, blog_post_id):
    blog_post = BlogPost.objects.filter(id=blog_post_id).first()
    return render(request, 'blogapp/about.html')
