from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Author
def home(request):
    ctx  ={
        'books':Book.objects.all(),
        'authors':Author.objects.all(),
    }
    
    return render(request, 'books/home.html',ctx)
def pools(request):
   
    return render(request, 'books/pools.html',)

