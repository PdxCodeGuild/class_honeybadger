from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import urlShort
from .pw_gen import password


def index(request):
    urls = urlShort.objects.all()
    domain = request.META['HTTP_HOST']

    context = {
        "urls":urls,
        "domain": domain,
    }
    return render(request, "lab_03_urlshort/index.html", context)
    

def save_url(request):
    pw = password()
    long_url = request.POST["long_url"]
    
    new_url = urlShort(
            url_long = long_url,
            url_code = pw,
    )
    
    new_url.save()
    return HttpResponseRedirect(reverse('lab_03_urlshort:index'))


def redirect_url(request, code):
    # look up the record with the given code
    links = urlShort.objects.get(url_code=code)

    # redirect to that record's long url
    return redirect(links.url_long)