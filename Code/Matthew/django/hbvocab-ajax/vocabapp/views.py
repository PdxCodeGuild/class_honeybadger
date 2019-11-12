from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import VocabItem


def index(request):
    return render(request, 'vocabapp/index.html')

def get_data(request):
    items_db = VocabItem.objects.order_by('word')
    items = []
    for item_db in items_db:
        items.append({
            'word': item_db.word,
            'definition': item_db.definition
        })
    return JsonResponse({'items': items})

def save_item(request):
    data = json.loads(request.body)
    word = data['word']
    definition = data['definition']
    item = VocabItem(word=word, definition=definition)
    item.save()
    return HttpResponse('ok')