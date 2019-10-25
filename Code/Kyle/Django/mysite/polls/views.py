from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'index': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html')

def results(request, question_id):
    return HttpResponse(f'Youre looking at the results of question')

def vote(request, question_id):
    return HttpResponse('youre voting on question %s' % question_id)
