from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shorten
import string
import random



def generate_code():
    lttrs = string.ascii_lowercase + string.ascii_uppercase
    nums = string.digits


    options = lttrs + nums
    code = ""

    for x in range(5):
        code += random.choice(options)
    return code


def index(request):
    URL_ToShortens = Shorten.objects.all()
    context = {
        'URL_ToShortens': URL_ToShortens
    }
    return render(request, 'shortapp/index.html', context)

def save_url(request):
    url = request.POST['longUrl']
    code = generate_code()
    new_url = Shorten(
            URL = url,
            code = code,
    )
    new_url.save()

    # create an instance of the model using the url and code
    # save it
    # redirect to the index page
    return HttpResponseRedirect(reverse('shortapp:index'))

def redirect_url(request, code):
    # look up the record with the given code
    # redirect to the long url inside the record
    return HttpResponseRedirect('redirecting to url with code ' + code)
