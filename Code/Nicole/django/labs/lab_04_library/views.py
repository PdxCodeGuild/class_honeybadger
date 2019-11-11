from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author

def index(request):
    books = Book.objects.all()

    context = {
        "books":books,
    }
    return render(request, "lab_04_library/index.html", context)
