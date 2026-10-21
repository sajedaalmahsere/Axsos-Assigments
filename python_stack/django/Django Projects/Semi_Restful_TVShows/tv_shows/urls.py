from django.urls import path
from . import views

urlpatterns =[
    path('', views.all_shows),
    path('add_show/',views.add_show),
    path('show/<int:id>/', views.show),
    # path('all_shows/', views.all_shows),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]