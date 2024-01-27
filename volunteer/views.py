from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import VolunteerProfile
from .forms import ProfileForm


def home(request):
    '''Redirects to landing page'''
    return render(request, 'index.html')


def get_verbose_name(name):
    '''Gets human readable version of field name'''
    session = VolunteerProfile._meta.get_field(name)
    verbose = session.verbose_name
    return verbose


def read_profile(request):
    '''
    Provides information that the volunteer has entered so that they
    know what is held on the database about them.
    Shows all the data that they have chosen without the other options.
    '''
    pk_logged_in = request.user.pk
    profile = get_object_or_404(VolunteerProfile, user_name_id=pk_logged_in)
    peeps = VolunteerProfile.objects.filter(user_name_id=pk_logged_in)
    peoples = peeps.values()
    skills = profile.skilled.values()
    true_pairs = [{key for key, value in people.items() if value is True}
                  for people in peoples]  # gets only sessions they tick
    sessions = []
    for true_pair in true_pairs:
        for pair in true_pair:
            pair = get_verbose_name(pair)
            sessions.append(pair)
    if 'activated' in sessions:
        sessions.remove('activated')
    context = {
        'peoples': peoples,
        'pk_logged_in': pk_logged_in,
        'true_pairs': true_pairs,
        'skills': skills,
        'sessions': sessions
    }
    return render(request, 'volunteer/read_profile.html', context)


def add_profile(request):
    '''
    Provides empty form for them to enter all their personal
    details, when available and what they want to do.
    '''
    form = ProfileForm
    pk_logged_in = request.user.pk
    vp = VolunteerProfile.objects.filter(user_name_id=pk_logged_in)
    VP_exists = vp.exists()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_name = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Profile in approval for volunteering!')
        return redirect('read')
    context = {
        'form': form,
        'VP_exists': VP_exists,
        }
    return render(request, 'volunteer/add_profile.html', context)


def edit_profile(request):
    '''
    Prepopulated form with what they have previously stored but the fields
    are editable so they can update it.
    '''
    pk_logged_in = request.user.pk
    available = get_object_or_404(VolunteerProfile, user_name_id=pk_logged_in)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=available)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated!')
            return redirect('read')
    form = ProfileForm(instance=available)
    context = {
        'form': form,
        'availabilities': available,
        'pk_logged_in': pk_logged_in
    }
    return render(request, 'volunteer/edit_profile.html', context)


def delete_profile(request):
    '''
    Allows delete only of the person logged in's account from modal
    confirmation.
    '''
    pk_logged_in = request.user.pk
    volunteer = get_object_or_404(User, id=pk_logged_in)
    volunteer.delete()
    messages.add_message(request, messages.WARNING, 'Profile deleted!')
    return redirect('index')
