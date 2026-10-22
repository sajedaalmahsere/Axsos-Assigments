from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, course):
        errors ={}
        course_name  = course.get('course_name', '')
        description = course.get('description', '')
        
        if len(course_name) < 5:
            errors['course_name'] = "The course name should be at least more than 5 characters"

        if len(description) <= 15:
            errors['description'] = "The course description should be at least more than 15 characters"
        
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()