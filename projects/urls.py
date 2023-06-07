from django.urls import path
from . import views



urlpatterns = [
  path('projects/', views.projectList, name = 'projects'),
  path('home/', views.home, name = 'home'),
  path('projects/<int:pk>', views.projectDetail, name ='project-detail'), 
  path('tasks/', views.taskList, name ='tasks'),
  path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),

 
]

