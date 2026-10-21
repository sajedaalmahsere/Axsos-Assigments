from django.shortcuts import render , redirect
from .models import Dojo,Ninja
# Create your views here.
def index(request):
    dojoes = Dojo.objects.all()
    context = {
        'dojoes': dojoes
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        request.session['state'] = state
        Dojo.objects.create(name = name,city =city, state=state)
        return redirect ('/')
    return redirect ('/')

def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo_id = request.POST['dojo_id']
        dojo = Dojo.objects.get(id= dojo_id)
        Ninja.objects.create(first_name=first_name ,last_name=last_name, dojo=dojo)
        return redirect('/')
    return redirect('/')

def list(request):
    dojoes = Dojo.objects.all()
    context = {
        'dojoes': dojoes
        # 'sajeda'
    }
    return render(request, 'index.html', context)

def hello(request):
    return render(request, 'hello.html')
