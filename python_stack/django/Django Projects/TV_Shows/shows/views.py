from django.shortcuts import render, redirect
from .models import Show
from login.models import User
from django.contrib import messages
# Create your views here.
def list_shows(request):
    movie = Show.objects.all()
    context ={
        'movie': movie,
    }
    return render(request, 'list_shows.html', context = context)


def shows(request):
    if request.method == 'POST':
        errors = Show.objects.basic_valedator(request.POST)
        if len(errors) > 0:
            for key in errors:
                messages.error(request, errors[key])
            return redirect('/shows/new/')
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        comments = request.POST['comments']
        user = User.objects.get(id=request.session['user_id'])
        Show.objects.create(
            title = title,
            network= network,
            release_date = release_date,
            comments = comments,
            user = user,
        )
        return redirect ('/shows/')
    return render(request, 'new.html')
    

def edit(request, id):
    movie = Show.objects.get(id = id)
    if request.method == 'POST':
        errors = Show.objects.basic_valedator(request.POST)
        if len(errors) > 0:
            for key in errors:
                messages.error(request, errors[key])
            return redirect(f'/shows/edit/{movie.id}/')
        else:
            movie.title = request.POST['title']
            movie.network = request.POST['network']
            movie.release_date = request.POST['release_date']
            movie.comments = request.POST['comments']
            movie.save()
            return redirect('/shows/')
    return render(request, 'edit.html', {'movie': movie})

def show(request, id):
    movie =Show.objects.get(id = id)
    user = User.objects.get(id=request.session['user_id'])
    context ={
        'movie' : movie,
        'user' : user
    }
    return render(request, 'details.html', context= context)

def delete (request, id):
    movie = Show.objects.get(id = id )
    movie.delete()
    return redirect('/shows/')
