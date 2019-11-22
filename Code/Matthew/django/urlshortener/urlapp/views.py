from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UrlShort
from string import ascii_letters, digits
from random import choice


def index(request):
    url_shorts = UrlShort.objects.order_by('date_created')
    
    # data = []
    # for url_short in url_shorts:
    #     parsed_uri = urlparse(url_short.user_url)
    #     domain = parsed_uri.netloc
    #     data.append({
    #         'user_url': url_short.user_url,
    #         'code': url_short.code,
    #         'domain': domain
    #     })
    host = request.scheme + '://' + request.META['HTTP_HOST']
    context = {
        'url_shorts': url_shorts,
        'host': host
    }
    return render(request, 'urlapp/index.html', context)



def save_url(request):
    # print(request.POST)
    url = request.POST['url']
    code = ''.join([choice(ascii_letters + digits) for i in range(6)])
    while UrlShort.objects.filter(code=code).exists():
        code = ''.join([choice(ascii_letters + digits) for i in range(6)])
    new_url = UrlShort(user_url=url, code=code)
    new_url.save()
    
    return HttpResponseRedirect(reverse('urlapp:index'))

def redirect_url(request, code):
    # use the code to find the UrlShort with that code
    url_short = UrlShort.objects.get(code=code)
    # redirect to the UrlShort's url
    return HttpResponseRedirect(url_short.user_url)
