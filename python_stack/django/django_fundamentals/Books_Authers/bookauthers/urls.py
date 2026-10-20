from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list),
    path('create_book/', views.create_book),
    path('view_book/<int:id>/', views.view_book),
    path('view_book/<int:id>/add_author/', views.add_author),
    path('create_author/', views.create_author),
    path('view_author/<int:id>/', views.view_author),
    path('view_author/<int:id>/add_book/', views.add_book),
]