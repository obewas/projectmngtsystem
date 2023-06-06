from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Task, Project
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



