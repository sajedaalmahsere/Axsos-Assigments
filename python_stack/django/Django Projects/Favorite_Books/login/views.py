from django.shortcuts import render , redirect
from .models import Register
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        errors = Register.objects.basic_validator(request.POST)
        if errors:
            for key in errors:
                messages.error(request,errors[key])
            return redirect('/')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        register = Register.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = hash_password,
        )
        request.session['register_id'] = register.id
        request.session['register_first_name'] = register.first_name
        return redirect('/')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        try:
            register = Register.objects.get(email=request.POST['email'])
            if register:
                if bcrypt.checkpw(request.POST['password'].encode(), register.password.encode()):
                    request.session['user_id'] = register.id
                    request.session['user_first_name']= register.first_name
                    return redirect('/books/')
        except:
            messages.error(request, f"The email {request.POST['email']} does not exist")
            return redirect('/')
        return redirect('/')
    return render(request, 'login.html')