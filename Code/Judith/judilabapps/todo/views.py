from django.shortcuts import render

from .models import Todoitem

def todo(request, **kwargs):
    context = {
        'message':'hello',
        'todos': Todoitem.objects.all()
    }
    return render(request, 'todo/base.html', context)
