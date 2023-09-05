from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Author
def contact(request):
    return render(request, 'books/contact.html')
def about(request):
    return render(request, 'books/about.html')

def home(request):
    ctx  ={
        'books':Book.objects.all()[:5],
        'authors':Author.objects.all(),
    }
    
    return render(request, 'books/home.html',ctx)
def AllBooks(request):
    ctx  ={
        'books':Book.objects.all(),
        
    }
    return render(request, 'books/allbooks.html',
                    ctx
                  )
def single_pool(request, pk):

    ctx = {'book' : Book.objects.get(id=pk),
            
           }
    try:
        author = Author.objects.get(id=ctx['book'].author_id)
    except:
        author = None
 
     #author = {'author':Author.objects.order_by(ctx['book'].author_id)}
    return render(request, 'books/single_pool.html', 
                {
                    'book':ctx['book'],
                    'author':author,
                }
                  )


