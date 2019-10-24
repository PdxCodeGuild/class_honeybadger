from django.shortcuts import render
from .models import ToDoItem
from django.template import loader
from django.urls import reverse
from .forms import ToDoForm


def index(request):
    latest_todo = ToDoItem.objects.order_by('-created_date')
    template = loader.get_template("lab_00_todo/index.html")
    completed_items = ToDoItem.objects.filter(
        completed=True).order_by('-completed_date')
    context = {
        "todo_list": latest_todo,
    }
    return render(request, "lab_00_todo/index.html", context)


def newtodo(request):
    todo_text = request.POST['todo_text']
    todo = ToDoForm(text=todo_text, completed=False)
    todo.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def todo_form(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data['todo_text']
            todo = Todo(text=todo_text)
            todo.save()
            form = ToDoForm()  # blank form
        # if the form is invalid, we just send it back to the template
    else:
        form = ToDoForm()
    return render(request, "lab_00_todo/index.html", {'form': form})
