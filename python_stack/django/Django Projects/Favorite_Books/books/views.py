from django.shortcuts import render , redirect
from .models import Book
# Create your views here.
def index(request):
    return render(request, 'add_book.html')

def add_book(request):
    if request.method == 'POST':
        uploaded_by_id = Book.objects.get(id=request.session['uploaded_by_id'])
        title = request.POST['title']
        desc = request.POST['desc']
        Book.objects.create(
            title = title, 
            desc = desc,
            uploaded_by_id = uploaded_by_id
            )
        return redirect('/books/')
    return redirect('/books/')