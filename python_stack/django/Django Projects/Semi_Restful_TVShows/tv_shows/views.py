from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
# def index(request):
#     return render(request, 'shows_list.html')

def all_shows(request):
    movie = Show.objects.all()
    context ={
        'movie': movie,
    }
    return render(request, 'shows_list.html', context = context)

def add_show(request):
    if request.method == 'POST':
        title = request.POST ['title']
        network = request.POST ['network']
        release_date = request.POST ['release_date']
        description = request.POST ['description']
        show = Show.objects.create(
            title = title,
            network = network, 
            release_date = release_date, 
            description = description
            )
        return redirect(f'/show/{show.id}/')
    return render(request, 'add_show.html')

def show(request, id):
    movie =Show.objects.get(id = id)
    if request.method == 'POST':
        movie.updated_at = request.POST['updated_at']
        return redirect(f'/show/{movie.id}/')
    context ={
        'movie' : movie,
    }
    return render(request, 'show_movie.html', context= context)

def edit(request, id):
    movie = Show.objects.get(id = id)
    
    if request.method == 'POST':
        movie.title = request.POST['title']
        movie.network = request.POST['network']
        movie.release_date = request.POST['release_date']
        movie.description = request.POST['description']
        movie.save()
        return redirect(f'/show/{movie.id}/')
    return render(request, 'edit.html', {'movie': movie})

def delete (request, id):
    movie = Show.objects.get(id = id)
    movie.delete()
    return redirect('/')
