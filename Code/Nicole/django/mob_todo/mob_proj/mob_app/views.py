from django.shortcuts import render, reverse
from .models import TodoList, TodoItem
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


def index(request):
    lists = TodoList.objects.all().order_by("name")
    
    context = {
        "lists": lists,
    }
    return render(request, "mob_app/index.html", context)


def new_todo(request):
    text = request.POST['new_text']
    list_id = request.POST['list_type']
    my_image = request.FILES['my_image']
    
    list = TodoList.objects.get(id=list_id)
    
    if 'urgent' in request.POST:
        urgent = True
    else:
        urgent = False

    new_item = TodoItem(
            text = text,
            list = list,
            urgent = urgent,
            my_image = my_image,
    )
    
    new_item.save()

    return HttpResponseRedirect(reverse('mob_app:index'))


def details(request, list_id):
    list_detailz = TodoList.objects.get(id=list_id)
    nav_list = TodoList.objects.all().order_by("name")
    ordered_items = list_detailz.items.order_by('date_completed', '-urgent')
    
    context = {
        'list_detailz': list_detailz,
        'lists': nav_list,
        'items': ordered_items,
    }
    
    return render(request, "mob_app/details.html", context)
    

def completed(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.date_completed = timezone.now()
    
    item.save()
    
    return HttpResponseRedirect(reverse('mob_app:details', args=[item.list.id]))


def delete_completed(request, list_id):
    list = TodoList.objects.get(id=list_id)
    
    for item in list.items.all():
        if item.date_completed:
            item.delete()
    
    return HttpResponseRedirect(reverse('mob_app:details', args=[list_id]))
        
    