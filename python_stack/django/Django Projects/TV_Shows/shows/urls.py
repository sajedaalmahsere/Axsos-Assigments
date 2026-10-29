from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list_shows),
    path('new/', views.shows),
    path('edit/<int:id>/', views.edit),
    path('show/<int:id>/', views.show),
    path('delete/<int:id>/', views.delete),
]