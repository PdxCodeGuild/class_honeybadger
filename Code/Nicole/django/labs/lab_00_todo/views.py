from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem
from django.template import loader
from django.utils import timezone


def index(request):
    latest_todo = ToDoItem.objects.order_by('-created_date').filter(completed=False)
    completed_items = ToDoItem.objects.filter(
        completed=True).order_by('-completed_date')
    context = {
        "todo_list": latest_todo,
        "completed_list" : completed_items
    }
    return render(request, "lab_00_todo/index.html", context)


def complete_todo(request):
    # get the item id from the database:
    item_id_shark = request.POST["item_id_llama"]
    # get the row using the item id in the database
    todo_item = ToDoItem.objects.get(id=item_id_shark)
    # change the values 
    todo_item.completed = True
    todo_item.completed_date = timezone.now()
    # save the item
    todo_item.save()
    return HttpResponseRedirect(reverse('lab_00_todo:index'))
    

def add_todo(request):
    print("=" * 100)
    print(request.POST)
    add_todo_shark = request.POST["add_todo_llama"]
    todo_item = ToDoItem(description_text = add_todo_shark,
                        completed=False,
                        created_date=timezone.now(),
                        )
    # todo_item = ToDoItem.objects.get(id=add_todo_shark)
    # todo_item.completed = False
    # todo_item.created_date = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('lab_00_todo:index'))


def delete_todo(request):
    delete_item_id = request.POST["delete_id_llama"]
    delete_item = ToDoItem.objects.get(id=delete_item_id)
    delete_item.delete()

    return HttpResponseRedirect(reverse('lab_00_todo:index'))


def undo_todo(request):
    print("=" * 100)
    print(request.POST)
    undo_item_shark = request.POST["undo_item_id"]
    undo_item = ToDoItem.objects.get(id=undo_item_shark)
    undo_item.completed = False
    undo_item.completed_date = None
    undo_item.save()
    return HttpResponseRedirect(reverse('lab_00_todo:index'))