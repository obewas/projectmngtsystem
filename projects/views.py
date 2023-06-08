from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Task, Project
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy

# Create your views here.
def currentTime(request):
	current_date_time = datetime.datetime.now()
	return HttpResponse(f"The time now is: {current_date_time}")


def home(request):
    return render(request, 'base.html')
 
class ProjectListView(ListView):
   model = Project
   template_name = 'projects.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'project_create_form.html'
    success_url = reverse_lazy('projects')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_update_form.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('projects')

class TaskListView(ListView):
   model = Task
   template_name = 'tasks.html'

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create_form.html'
    success_url = reverse_lazy('tasks')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update_form.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasks')
 

def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks':project_tasks}
   return render(request, 'project-detail.html',context)

def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'task-detail.html',context)

def joinTask(request,pk):
   task =Task.objects.get(id=pk)
   task.assignee=request.user
   task.save()
   return redirect('tasks')

   

