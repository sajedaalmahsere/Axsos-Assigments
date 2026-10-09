from django.shortcuts import render , redirect , HttpResponse

# Create your views here.
def create(request):
    return redirect('/')

def root(request):
    return redirect('/blogs/')

def blogs(request):
    return render(request, "index.html")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to later display a list of all blogs2")

def show(request,number):
    return HttpResponse(f"placeholder to display a blog number:{number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect('/blogs/')