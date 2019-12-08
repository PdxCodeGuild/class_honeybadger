from django.shortcuts import render, reverse
from django.http import HttpResponse , HttpResponseRedirect
import string
import random
from .models import UrlCode
# Create your views here.


def code_gen():
    alphabet = list(string.ascii_lowercase)

    url_code = ''
    for i in range(5):
        url_code  += random.choice(alphabet)
    return url_code


def index(request):
    context = {
<<<<<<< HEAD
        'message': 'Enter your URL'
=======
        'message': 'Enter your URL',
        'url_shorts': UrlCode.objects.all()
>>>>>>> 26d2ca2e849b96cb19d7537771ce4e0481d57852
    }
    return render(request, 'urlapp/index.html', context)


def save_url(request):
    print(request.POST) # form data
    code = code_gen()
    url = request.POST['url']
    urlcode = UrlCode(url=url, code=code)
    urlcode.save()
    # create an instance of the model
    # save it
    # redirect back to the index page
    return HttpResponseRedirect(reverse('urlapp:index'))


def redirect_url(request, code):
    # url_id = request.POST['url_id']
    long_url = UrlCode.objects.get(code=code)

    # look up the record with the given code
    # redirect to the long url
    return HttpResponseRedirect(long_url.url)
