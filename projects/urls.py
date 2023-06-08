from django.urls import path
from . import views



urlpatterns = [
  path('projects/', views.ProjectListView.as_view(), name = 'projects'),
  path('home/', views.home, name = 'home'),
  path('projects/<int:pk>', views.projectDetail, name ='project-detail'), 
  path('tasks/', views.TaskListView.as_view(), name ='tasks'),
  path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),
  path('create-task/', views.TaskCreateView.as_view(), name ='create-task'),
  path('create-project', views.ProjectCreateView.as_view(), name ='create-project'),
  path('update-task/<int:pk>', views.TaskUpdateView.as_view(), name ='update-task'),
  path('update-project/<int:pk>', views.ProjectUpdateView.as_view(), name ='update-project'),
  path('delete-task/<int:pk>', views.TaskDeleteView.as_view(), name ='delete-task'), 
  path('delete-project/<int:pk>', views.ProjectDeleteView.as_view(), name ='delete-project'),
  path('join-task/<int:pk>', views.joinTask, name ='join-task'),
  


 
]

