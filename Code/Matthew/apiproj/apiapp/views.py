from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    context = {
        'message': 'hello world!',
        'fruits': ['apples', 'bananas', 'mangoes', 'pears']
    }
    return render(request, 'apiapp/index.html', context)
    # return HttpResponse('ok abc 123')

def getdata(request):
    data = {'message': 'hello world!'}
    return HttpResponse(str(data))