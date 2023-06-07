from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Task, Project
from django.shortcuts import get_object_or_404

# Create your views here.
def currentTime(request):
	current_date_time = datetime.datetime.now()
	return HttpResponse(f"The time now is: {current_date_time}")


def home(request):
    return render(request, 'base.html')
 

def projectList(request):
   projects = Project.objects.all()
  
   context = {'projects':projects}
   return render(request, 'projects.html',context)

def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks':project_tasks}
   return render(request, 'project-detail.html',context)


def taskList(request):
    user_tasks =Task.objects.filter(assignee=request.user)
    tasks = Task.objects.filter(assignee=None)
 
    context = {'tasks':tasks,'user_tasks':user_tasks}
    return render(request, 'tasks.html',context)

def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'task-detail.html',context)