from django.shortcuts import render , redirect
from .models import Book , Author

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Book.objects.create(title = title, desc = description)
        return redirect ('/')
    return redirect('/')

def list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books' : books,
        'authors': authors

    }
    return render(request, 'index.html', context = context)

def view_book(request, id):
    book = Book.objects.get(id = id)
    author = Author.objects.all()
    context = {
        'book': book,
        'authors': author
    }
    return render(request, 'view_book.html', context=context)

def add_author(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id = id)
        author_id = request.POST['author']
        author = Author.objects.get(id = author_id)
        author.books.add(book)
    return redirect(f'/view_book/{id}/add_author/')


def create_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(first_name = first_name, last_name = last_name , notes = notes)
        return redirect ('/')
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'author.html', context)

def view_author(request, id):
    author = Author.objects.get(id = id)
    book = Book.objects.all()
    context = {
            'books': book,
            'author': author
        }
    return render(request, 'view_author.html', context=context)
    
def add_book(request, id):
    if request.method == 'POST':
        author = Author.objects.get(id = id)
        book_id = request.POST['book']
        book = Book.objects.get(id = book_id)
        author.books.add(book)
        return redirect(f'/view_author/{id}/')
    
    

