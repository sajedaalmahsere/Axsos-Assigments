from django.shortcuts import render , redirect
from .models import User
import bcrypt
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        # Check if this is the first user
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for key in errors:
                messages.error(request,errors[key])
                return redirect('/register/')
            
        if User.objects.count() == 0:
            user_level = 9  # Admin
        else:
            user_level = 1  # Normal User

        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=hashed_password,
            user_level=user_level
        )
        return redirect('/signin/')
    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            if user:
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['user_id'] = user.id
                    request.session['user_first_name']= user.first_name
                    request.session['user_level'] = user.user_level
                    if user.user_level == 9:
                        return redirect('/dashboard/')
                else:
                    return redirect('/profile/')
        except:
            messages.error(request, f"The email {request.POST['email']} does not exist")
            return redirect('/')
        return redirect('/')
    return render(request, 'signin.html')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/signin/')

    if request.session.get('user_level') != 9:
        return redirect('/profile/')

    users = User.objects.all()

    return render(request, 'dashboard.html', {
        'users': users
    })