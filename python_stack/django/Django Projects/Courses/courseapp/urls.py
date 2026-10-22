from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list),
    path('add_course/', views.add_course),
    # path('course_list/', views.course_list),
    path('remove_course/<int:id>/', views.remove_course),
    path('delete/<int:id>/', views.remove),
]