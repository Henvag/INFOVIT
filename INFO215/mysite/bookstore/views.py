from django.shortcuts import render
from .models import Add_book
# Create your views here.
def add (request):
    post = Add_book.objects.all()
    context = {
    'bookstore' :post
    }
    return render(request, "index.html", context)

#s