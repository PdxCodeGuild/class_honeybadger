from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

from . import pwgen

def pwgen_view(request):
    
    pw = pwgen.password(5, 5, 5, 5)
    return HttpResponse(pw)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    question = Question.objects.filter(id=question_id).first()
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

# <QueryDict: {'csrfmiddlewaretoken': ['FviUEXyfDUDkXrOE1MWoL8nOy4eYbqxfwTN1KIZx3m4YcLqxAL5PEKlVWuI75d5e'], 'mytext': ['llama'], 'mypassword': ['llama123'], 'cb1': ['on'], 'rb': ['3'], 'mydate': ['2019-10-24'], 'mytime': ['00:26'], 'mycolor': ['#4141f1']}>
def vote(request, question_id):
    print(request.POST)
    mytext_anything = request.POST['mytext']
    mypassword_anything = request.POST['mypassword']
    cb1_anything = 'cb1' in request.POST
    cb2_anything = 'cb2' in request.POST
    rb_anything = request.POST['rb']
    mydate_anything = request.POST['mydate']
    mytime_anything = request.POST['mytime']
    
    # print(mytext_llama)
    return HttpResponse("You're voting on question " + str(question_id))
