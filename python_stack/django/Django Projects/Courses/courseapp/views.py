from django.shortcuts import render , redirect
from .models import Course
from django.contrib import messages
# Create your views here.


def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            course_name = request.POST['course_name']
            description = request.POST['description']
            Course.objects.create(
                course_name = course_name, 
                description = description
                )
            return redirect('/')
    return redirect ('/')

def course_list(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render( request,'course.html', context=context)

def remove_course(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'remove.html', {'course': course})

def remove(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')


