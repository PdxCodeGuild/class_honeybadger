from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# def index(request):
#   return HttpResponse('hello world!')


def index(request):
    context = {
        'message': 'Hello World!',
        'contacts': Contact.objects.all(),
    }
    return render(request, 'contactapp/index.html', context)


def detail(request, contact_id):
    return HttpResponse('detail page with id ' + str(contact_id))
