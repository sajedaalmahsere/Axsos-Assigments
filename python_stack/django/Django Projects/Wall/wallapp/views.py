from django.shortcuts import render , redirect
from .models import Message , Comment
from login.models import User
# Create your views here.
def index(request):
    return render(request,'the_wall.html')

def message(request):
    if request.method == 'POST':
        message = request.POST['message']
        # retrieves the logged-in user's ID
        user_id = User.objects.get(id=request.session['user_id'])
        Message.objects.create(
            message = message,
            user_id = user_id,
            )
        return redirect('/wall/')
    return redirect('/wall/')

def list_message(request):
    #(-) descending order
    message = Message.objects.all().order_by('-created_at')
    context = {
        'messages': message,
    }
    return render(request, 'the_wall.html', context = context)

def comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        message_id = request.POST['message_id']

        user_id = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=message_id)

        Comment.objects.create(
            comment = comment,
            user_id = user_id,
            message = message,
        )
        return redirect('/wall/')
    return redirect( '/wall/')

def list_comment(request, id):
    message = Message.objects.get(id = id)
    comment = Comment.objects.all().order_by('-created_at')
    context ={
        'message': message,
        'comments': comment,
    }
    return render(request, 'the_wall.html', context)

def logout(request):
    request.session.flush()
    return redirect('/login/')
