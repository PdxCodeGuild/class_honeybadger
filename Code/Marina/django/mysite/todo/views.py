from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def index(request):

    todos = TodoItem.objects.filter(completed_date__isnull=True)
    todos_completed = TodoItem.objects.filter(completed_date__isnull=False)
    context = {'todos': todos, 'todos_completed': todos_completed}
    return render(request, 'todo/index.html', context)

def savetodo(request):
    todo_text = request.POST['todo_id']
    todo_item = TodoItem(text=todo_text, completed_date=None)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def completetodo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def completetodoq(request):
    todo_id = request.GET['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))
