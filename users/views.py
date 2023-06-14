from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)

def registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('home')
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm

def logout_user(request):
   logout(request)
   return redirect("login")


@login_required
def update_profile(request):
   if request.method == 'POST':
       form = ProfileForm(request.POST, instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('tasks')
   else:
       form = ProfileForm(instance=request.user.profile)
  
   context = {'form': form}
   return render(request, 'users/profile-update-form.html', context)

