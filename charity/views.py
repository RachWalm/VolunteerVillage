from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CharityProfile
from .forms import CharityForm

# Create your views here.


def home(request):
    return render(request, 'index.html')

def add_charity(request):
    form= CharityForm
    if request.method == 'POST':
        # form_data_co = {
        #     'user_name': request.user,
        # }

        print('test')
        form = CharityForm(request.POST) 
        if form.is_valid(): 
            print('tesst5')
            # profile = form.save(commit=False)
            # profile.user_name = request.user
            form.save()
            print(form)
            print('test4')
        else:
            print(form.errors)
        return redirect('dashboard')
    context = {
        'form': form,
        }
    return render(request, 'coordinator/add_profile.html', context)
from django.shortcuts import render

# Create your views here.
