from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    return render(request, 'index.html')

def process(request):

    if request.method == 'POST':
        
        if request.POST['place'] == 'farm':
            random_number = random.randint(10,20)
        elif request.POST['place'] == 'cave':
            random_number = random.randint(2,5)
        elif request.POST['place'] == 'house':
            random_number = random.randint(5,10) 
        else:
            random_number = random.randint(-50,50)
            
        request.session['gold'] += random_number

        return redirect('/')
