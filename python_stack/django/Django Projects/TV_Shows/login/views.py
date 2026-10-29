from django.shortcuts import render , redirect
from .models import User
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for key in errors:
                messages.error(request,errors[key])
            return redirect('/')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = hashed_password,
        )
        request.session['user_id'] = user.id
        request.session['user_first_name']= user.first_name
        return redirect('/')
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            if user:
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['user_id'] = user.id
                    request.session['user_first_name']= user.first_name
                    return redirect('/shows/')
        except:
            messages.error(request, f"The email {request.POST['email']} does not exist")
            return redirect('/')
        return redirect('/')
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')