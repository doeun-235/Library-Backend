from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from app.models import Book_owned, Book_disposal 

from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def owned_index(request:HttpRequest)->HttpResponse:
    qs = Book_owned.objects.all()
    
    return render(
        request,'app/owned/index.html',{
            'book_list' : qs,
        })

def owned_detail(request:HttpRequest,pk:int) -> HttpResponse:
    book = get_object_or_404(Book_owned,pk=pk)

    return render(
        request,
        'app/owned/book_detail.html',
        {'Book':book,},
    )    



# Create your views here.
