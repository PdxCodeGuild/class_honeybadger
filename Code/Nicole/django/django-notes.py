# 1. Start project: Create a main project folder. This will contain your apps. Name doesn't matter (it can be renamed without problems).

    django-admin startproject <mysite>


##########################################
# 2. cd into the <mysite> directory. You can now run the server:

    python manage.py runserver
    

##########################################
# 3. cd into the folder that containst the manage.py file. Then create an app:

    python managey.py startapp <yourappname>


##########################################
# 4. Add HttpResponse code to the views.py file in the app folder:

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Type some text here.")


##########################################
# 5. Create a urls.py file in the app folder.


##########################################
# 6. Add code to the urls.py file that was just created:

    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.index, name="index")
    ]


##########################################
# 7. Add code to the <mysite>/urls.py file. This tells the project to include the urls from the app that was created.

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('yourappname/', include('yourappname.urls')),
        path('admin/', admin.site.urls),
    ]


##########################################
# 8. Set up the database. Go to the <mysite>/settings.py file. Set the timezone:

    - US/Pacific
    - US/Central


##########################################
# 9. In the terminal, migrate the database:

    python manage.py migrate


##########################################
# 10. Create models (classes in Python). Go to the app folder and accewss the models.py file:

    from django.db import models
    
    # these are arbitrary classes, only for this specific example (the "polls" tutorail on the Django website)
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)


##########################################
# 11. Add the app that was created into the installed apps in the settings.py file. The app name is located in the apps.py file within the app folder. This is example code that is added to the settings.py file:

    INSTALLED_APPS = [
        'lab_01_polls.apps.Lab01PollsConfig', # this corresponsw with "yourappname"
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]


##########################################
# 12. In the terminal, run a command. For example:

    python manage.py makemigrations lab_01_polls


##########################################
# 13. Run migrate to create the models in the database:

    python manage.py migrate
    

##########################################
# 14. Create admin superuser:

    python manage.py createsuperuser
    
# Log in to the admin on the server (/admin).


##########################################
# 15. Make the app modifieable in the admin. Go to the yourappname/admin.py and edit it with the following code (the exact models will vary depending on the classes/models created in step 10):

    from django.contrib import admin
    from .models import Question

    admin.site.register(Question)
    
# Now the models are located in both the admin page and the database.


##########################################
# 16. Adding more views. Go to the yourappname/views.py file, for example:

    def detail(request, question_id):
        return HttpResponse(f"You're looking at question {question_id}")

    def results(request, question_id):
        response = f"You're looking at the results of {question_id}"
        return HttpResponse(response)

    def vote(request, question_id):
        return HttpResponse(f"You're voting on question {question_id}")

# NOTE: This is all just testing the setup. The response here is only showing text on the page.


##########################################
# 17. Add these views to the yourappname.urls module:

    from django.urls import path
    from . import views

    urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # ex: /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]


##########################################
# 18. You can make the appname/views.py file more robust. Right now it is only serving simple text. However, you can plug other information into it. Don't forget to import the .models at the top, for example:

    from django.http import HttpResponse
    from .models import Question

    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        output = ", ".join([q.question_text for q in latest_question_list])
        return HttpResponse("Hello, world. You're at the lab_01_polls index")


##########################################
# 19. Create a templates folder within the yourappname folder. Then, create another folder the same name as <yourappname>. Then, create an index.html file within that folder:

    yourappname/templates/yourappname/index.html


##########################################
# 20. This HTML file can be filled with variables from the views.py and models.py files. For example:

    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/lab_01_polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}


##########################################
# 21. Update the views.py file to include the template:

    from django.template import loader
    
    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        # output = ", ".join([q.question_text for q in latest_question_list])
        template = loader.get_template("lab_01_polls/index.html")
        context = {
            "latest_question_list": latest_question_list,
        }
        return HttpResponse(template.render(context, request))

# Alternately, you can use the render() shortcut:

    from django.shortcuts import render
    from .models import Question

    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        context = {
            "latest_question_list": latest_question_list,
        }
        return render(request, 'polls/index.html', context) # Uses "render" here
        
        
##########################################
# 22. Create a 404 exception. For example:

    def detail(request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'lab_01_polls/detail.html', {'question': question})


##########################################
# 23. 