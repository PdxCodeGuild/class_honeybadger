from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import TodoItem, TodoItemType


def index(request):
    todo_items = TodoItem.objects.order_by('date_completed', 'date_created')
    todo_types = TodoItemType.objects.order_by('name')
    context = {
        'todo_items': todo_items,
        'todo_types': todo_types
    }
    return render(request, 'todoapp/index.html', context)

def other(request):
    return render(request, 'todoapp/other.html', {})


def save_todo(request):
    
    print(request.POST)
    todo_text = request.POST['todo_text']
    todo_type_ids = request.POST.getlist('todo_type_ids')
    
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    
    for todo_type_id in todo_type_ids:
        todo_type = TodoItemType.objects.get(id=todo_type_id)
        todo_item.types.add(todo_type)
    
    return HttpResponseRedirect(reverse('todoapp:index'))
    
def complete_todo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
    