from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    return render(request, 'polls/detail.html', {'question':question})

    # return HttpResponse('fuck')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    print(request.POST)
    myname = request.POST['myname']
    print(myname)
    return HttpResponse("You're voting on question %s." % question_id)