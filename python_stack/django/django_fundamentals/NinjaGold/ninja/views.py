from django.shortcuts import render, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'index.html')


def process(request):
    if request.method == 'POST':
        place = request.POST.get('place')

        if place == 'farm':
            amount = random.randint(10, 20)
        elif place == 'cave':
            amount = random.randint(5, 10)
        elif place == 'house':
            amount = random.randint(2, 5)
        elif place == 'quest':
            amount = random.randint(-50, 50)
        else:
            return redirect('/')

        request.session['gold'] += amount

        if amount >= 0:
            activity = f'You earned {amount} gold from the {place}!'
        else:
            activity = f'You lost {abs(amount)} gold from the {place}!'

        activities = request.session['activities']
        activities.insert(0, activity)
        request.session['activities'] = activities

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')