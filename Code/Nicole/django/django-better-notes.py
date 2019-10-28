##########################################
# SETTING UP THE PROJECT, APPS, ROUTEST, AND VIEWS
##########################################

# 1. Start project:

    django-admin startproject <projectname>


# 2. CD into the project

# 3. Create app:

    python manage.py startapp <appname>


# 4. Add app to the project settings.py file. Update the timezone as well.

# 5. Create a view in the app views.py folder:
    
    Easiest way to check is to create an HttpResponse with a string to test the server, for example:
    
    from django.http import HttpResponse
    
    def index(request):
        return HttpResponse("This is the app inded page")
    

# 6. Create and go to urls.py in the APP folder:

    from . import views
    from django.urls import path
    
    app_name = "<appname>"
    urlpatterns = [
        path("", views.index, name = "index")
    ]


# 7 Go to the urls.py in the PROJECT folder:

    path("blog/", include("<appname>.urls"))
    # this takes us to 8000/blog.html
    
    # <<or>>
    
    path("", include("<appname>.urls"))
    # this takes us to the main website url (not a /something website)


# 8. Create templates for each view:

    - Create "templates" folder in the app folder
    - Create a folder the same name as the app
    - Create an .html file within that folder


# 9. In the app views.py file, change the return to "render":

    from django.shortcuts import render
    
    def index(request):
        return render(request, "<appname>/filename.html")
    


##########################################
# CREATING MODELS (CLASSES)    
##########################################


# 10. Go to models.py file within the app. For example:

    class BlogPostType(models.Model):
        name = models.CharField(max_length=100)
        # this creates a field specifically for the foreign key set in the class below

    class BlogPost(models.Model):
        title = models.CharField(max_length=200)
        body = models.TextField()
        type = models.ForeignKey(BlogPostType, on_delete=models.PROTECT, related_name="posts")

# 11. Import the models in the app admin.py file. For example:

    from .models import BlogPost, BlogPostType
    
    admin.site(register(BlogPost))
    admin.site(regsiter(BlogPostType))
    

# 12. In the app's views.py file, import the models. For example:

    from .models import BlogPost, BlogPostType
    
    # then you can use the models within the views to populate the rendered HTML, such as:
    
    def inded(request):
        blog_posts = BlogPost.objects.order_by("-published_date")
        context = {
            "blog_posts" : blog_posts,
        }
        return render(request, "blogapp/index.html", context)
        

# 13. Add the info to the HTML template file, such as:

    # ...
    {% for blog_post in blog_posts %}
    <p> {{ blog_post.title }} </p>
    {% endfor %}
    
    # here, the "blog_posts" comes from the views.py file, and the "...title" comes from the models.py file.

    # You can also add filters to your values, such as {{ ..... | title }} (that capitalizes the first letter in each word)


##########################################
# Custom management commands
##########################################

# 1. Create a "management" folder inside the app
# 2. Create a "commands" folder insid the management folder
# 3. Create a .py file inside to create a command/script for your app


##########################################
# Template inheritance
##########################################

# Create a file to be the main template, such as base.html
# This is where you build the main template for your child templates

{% block <aribtraryname> %}
{% endblock %}

# Add this to the top of your other html files:

{% extends "appname/base.html" %}

# Then the only other thing that goes into the other html files is the content (no head, etc.)


##########################################
# Forms
##########################################

# Five important parts of a form:

<form action="{% url <appname>:<urlname>}" method="post">

    - Action # the app to which we want to submit the form data, a separate view that receives the form submission and redirects to the form page
    - Method
    - {% csrf_token %} # cross-site request forgery
    - Inputs with name attributes # this turns the fields into key/value pairs
    - Submit button