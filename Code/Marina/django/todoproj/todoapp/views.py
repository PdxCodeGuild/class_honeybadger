from django.shortcuts import render,reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import ToDoPost

def index(request):
    todo_posts = ToDoPost.objects.order_by('date_posted')

    context = {
        'todo_posts': todo_posts,
    }
    return render(request, "todoapp/index.html", context)

def detail(request, todo_post_slug):
    single_do = ToDoPost.objects.get(slug=todo_post_slug)
    context = {
        'single_do': single_do
    }
    return render(request, 'todoapp/detail.html', context)

def create_todopost(request):
    print(request.POST)
    title = request.POST['title']
    body = request.POST['body']
    slug = request.POST['slug']

    todo_post = ToDoPost(title = title,
                        slug = slug,
                        body = body)

    todo_post.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
