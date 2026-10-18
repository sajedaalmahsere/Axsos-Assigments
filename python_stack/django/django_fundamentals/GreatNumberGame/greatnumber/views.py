from django.shortcuts import render , redirect

# Create your views here.
import random


def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0

    return render(request, 'index.html')


def guess(request):
    if request.method == 'POST':
        if 'number' not in request.session:
            return redirect('/')
        number = request.session['number']
        guess_number = int(request.POST['guess'])
        request.session['attempts'] += 1
        if guess_number == number:
            result = 'correct'
        elif guess_number < number:
            result = 'low'
        else:
            result = 'high'
        if result == 'correct':
            request.session['result'] = 'correct'
        else:
            request.session['result'] = result
        return redirect('/')
    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')