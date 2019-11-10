from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import Contact

def index(request):
    contact = Contact.objects.order_by('last_name')
    context = {
        'contact_names': contact_names
    }
    return render(request, 'contactsapp/index.html', context)

def add_contact(request):
    contact_first_name = request.POST["contact_first_name"]
    contact_last_name = request.POST["contact_last_name"]
    contact_birthday = request.POST['contact_birthday']
    contact_phone = request.POST["contact_phone"]
    contact_cell = "contact_cell" in request.POST

    new_contact = Contact(
                first_name = contact_first_name,
                last_name = contact_last_name,
                birthday = contact_birthday,
                phone_number = contact_phone,
                is_cell = contact_cell
    )

    new_contact.save()

    return HttpResponseRedirect(reverse('contactsapp:index'))
