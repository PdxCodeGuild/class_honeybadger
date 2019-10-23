# lab_01_polls/views.py

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("id")[:5]
    template = loader.get_template("lab_01_polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "lab_01_polls/index.html", context)

    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'lab_01_polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "lab_01_polls/results.html", { "question" : question})

        

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'lab_01_polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('lab_01_polls:results', args=(question.id,)))
    