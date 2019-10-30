from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact

def index(request):
    contact_names = Contact.objects.order_by("last_name")
    context = {
        "contact_names": contact_names
    }
    
    return render(request, "lab_02_contacts/index.html", context)
    

def add_contact(request):
    print("=" *100)
    print(request)
    
    contact_first_name = request.POST["contact_first_name"]
    contact_last_name = request.POST["contact_last_name"]
    contact_birthday = request.POST["contact_birthday"]
    contact_phone = request.POST["contact_phone"]
    contact_cell = "contact_cell" in request.POST # if the key is in the dictionary, it will be true, otherwise it's false if unchecked (specifically for checkbox inputs)
    
    new_contact = Contact(
                first_name = contact_first_name,
                last_name = contact_last_name,
                birthday = contact_birthday,
                phone_number = contact_phone,
                is_cell = contact_cell
    )
    
    new_contact.save()
    
    return HttpResponseRedirect(reverse('lab_02_contacts:index'))