from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import VolunteerProfile, SkillChoices
from .forms import ProfileForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def read_profile(request):
    pk_logged_in = request.user.pk
    profile = get_object_or_404(VolunteerProfile, user_name_id = pk_logged_in)
    people = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).values()
    skills = profile.skilled.values()
    true_pairs = [{key for key, value in available.items() if value is True} for available in people]
    context = {
        'people': people,
        'pk_logged_in': pk_logged_in,
        'true_pairs': true_pairs,
        'skills': skills
    }
    return render(request, 'volunteer/read_profile.html', context)

def add_profile(request):
    form= ProfileForm
    if request.method == 'POST':
        
        form = ProfileForm(request.POST) 
        if form.is_valid(): 
            print(form.is_valid)
            print('tesst5')
            profile = form.save(commit=False)
            profile.user_name = request.user
            profile.name = request.user
            form.save()
            print('test6')
            messages.add_message(request, messages.SUCCESS, 'Profile sent for approval -  then you will be matched!')
        else:
            print('testelse')
            print(form.errors)
        return redirect('read')
    context = {
        'form': form,
        }
    return render(request, 'volunteer/add_profile.html', context)



def edit_profile(request):
    pk_logged_in = request.user.pk
    availabilities = get_object_or_404(VolunteerProfile, user_name_id =pk_logged_in)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=availabilities)
        if form.is_valid():
            form.save()
            return redirect('read')
    form = ProfileForm(instance = availabilities)
    context = {
        'form': form,
        'availabilities': availabilities,
        'pk_logged_in': pk_logged_in
    }
    return render(request, 'volunteer/edit_profile.html', context)

def delete_profile(request):
    pk_logged_in = request.user.pk
    user = get_object_or_404(User, id=pk_logged_in)
    user.delete()
    return redirect('index')

# messages.add_message(request, messages.SUCCESS, 'Comment deleted!')