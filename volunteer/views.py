from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import VolunteerProfile, SkillChoices
from role.models import Role
from .forms import ProfileForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def get_verbose_name(name):
    session = VolunteerProfile._meta.get_field(name)
    verbose = session.verbose_name
    return verbose

def read_profile(request):
    pk_logged_in = request.user.pk
    profile = get_object_or_404(VolunteerProfile, user_name_id = pk_logged_in)
    peoples = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).values()
    skills = profile.skilled.values()
    true_pairs = [{key for key, value in people.items() if value is True} for people in peoples]
    sessions =[]
    for true_pair in true_pairs:
        for pair in true_pair:
            pair = get_verbose_name(pair)
            sessions.append(pair)
    print(true_pairs)
    context = {
        'peoples': peoples,
        'pk_logged_in': pk_logged_in,
        'true_pairs': true_pairs,
        'skills': skills,
        'sessions': sessions
    }
    return render(request, 'volunteer/read_profile.html', context)

def add_profile(request):
    form= ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST) 
        if form.is_valid(): 
            profile = form.save(commit=False)
            profile.user_name = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile sent for approval -  then you will be matched!')
        else:
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
            messages.add_message(request, messages.SUCCESS, 'Profile Updated!')
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
    volunteer = get_object_or_404(VolunteerProfile, user_name_id=pk_logged_in)
    volunteer.delete()
    messages.add_message(request, messages.WARNING, 'Profile deleted!')
    return redirect('add')
