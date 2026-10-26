from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_message),
    path('message/', views.message),
    path('list_message/',views.list_message),
    path('comment/', views.comment),
    path('logout/', views.logout),
]