from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import SearchTerm

def index(request):
    return render(request, 'searchapp/index.html', {})


def get_search_terms(request):
    input = request.GET['input']
    terms = SearchTerm.objects.filter(text__startswith=input)[:10]
    data = {'terms': [term.text for term in terms]}
    return JsonResponse(data)
