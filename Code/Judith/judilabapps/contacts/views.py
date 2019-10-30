from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Contactitem

def index(request):
    contact_list = Contactitem.objects.all()
    
    context = {
        'contact_list': contact_list
                }
    return render(request, 'contacts/index.html', context)

def detail(request, item_id):
    item = Contactitem.objects.filter(id=item_id).first()
    
    if item.is_cell == True:
        is_cell = 'mobile'
    else:
        is_cell = 'home'

    context = {
        'item':item,
        'is_cell':is_cell
    }

    return render(request, 'contacts/detail.html', context)

def new(request):
    new_data = {
        'first_name':request.POST['first_name'],
        'last_name':request.POST['last_name'],
        'birthday':request.POST['birthday'],
        'phone_num':request.POST['phone_num'],
        'is_cell':request.POST['is_cell'],
        }

    if new_data['is_cell'] == 'on':
        new_data['is_cell'] = True
    else:
        new_data['is_cell'] = False

    new_con = Contactitem(first_name = new_data['first_name'],
                          last_name = new_data['last_name'],
                          birthday = new_data['birthday'],
                          phone_num = new_data['phone_num'],
                          is_cell = new_data['is_cell'] )
    new_con.save()
    return HttpResponseRedirect(reverse('contacts:index'))

def edit(request, item_id):
    item = Contactitem.objects.filter(id=item_id).first()

    new_data = {'first':request.POST['first'],
                'last':request.POST['last'],
                'birthday':request.POST['birthday'],
                'phone':request.POST['phone'],
                'is_cell':request.POST['is_cell']}
    
    item.first_name = new_data['first']
    item.last_name = new_data['last']
    item.birthday = new_data['birthday']
    item.phone_num = new_data['phone']
    item.is_cell = new_data['is_cell']

    item.save()

    return HttpResponseRedirect(reverse('contacts:detail', args=[item.id]))   