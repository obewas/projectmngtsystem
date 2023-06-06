from django.urls import path
from . import views



urlpatterns = [
  path('projects/', views.projectList, name = 'projects'),
  path('home/', views.home, name = 'home'),
 
]

