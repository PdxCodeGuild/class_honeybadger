from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author

def index(request):
    books = Book.objects.all()

    context = {
        "books":books,
    }
    return render(request, "lab_04_library/index.html", context)


def checkout(request, book_id):
    book_id = request.POST["book_checkout_id"]
    book_checkout = Book.objects.get(id=book_id)
    
    book_checkout.checked_out = True
    book_checkout.save()
    
    return HttpResponseRedirect(reverse('lab_04_library:index'))