from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("this is the equivelant of @app.route('/')!")