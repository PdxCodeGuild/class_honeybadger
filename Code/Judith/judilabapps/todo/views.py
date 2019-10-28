from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


from .models import Todoitem

def index(request, **kwargs):
    context = {
        'message':'hello',
        'todos': Todoitem.objects.all()
    }
    return render(request, 'todo/index.html', context)

def new_todo(request, **kwargs):
    todo_txt = request.POST['todo_txt']
    todo = Todoitem(body=todo_txt, completion_status=False)
    todo.save()
    return HttpResponseRedirect(reverse('todo:index'))

def complete_todo(request):
    todo_id = request.POST['todo_id']
    item = get_object_or_404(Todoitem, pk=todo_id)
    item.completion_status = True
    item.complete_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('todo:index'))
    