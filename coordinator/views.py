from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CoordinatorProfile
from .forms import ProfileFormCo

# Create your views here.

def pending(request):
    return render(request, 'coordinator/pending.html')

def dashboard(request):
    return render(request, 'coordinator/dashboard.html')

def home(request):
    return render(request, 'index.html')

def add_profile_co(request):
    form= ProfileFormCo
    if request.method == 'POST':
        form_data_co = {
            'user_name': request.user,
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
        }

        print('test')
        form = ProfileFormCo(form_data_co) 
        print(form.is_valid)
        if form.is_valid(): 
            print('tesst5')
            profile = form.save(commit=False)
            profile.user_name = request.user
            form.save()
            print(form)
            print('test4')
        else:
            print(form.errors)
        return redirect('pending')
    context = {
        'form': form,
        }
    return render(request, 'coordinator/add_profile.html', context)
