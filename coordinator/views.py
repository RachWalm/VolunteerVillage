from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import CoordinatorProfile
from volunteer.models import VolunteerProfile, SkillChoices
from role.models import Role
from charity.models import CharityProfile
from .forms import ProfileFormCo, ProfileFormCoUpdate, ProfileFormVolunteer


# Create your views here.

def pending(request):
    return render(request, 'coordinator/pending.html')

def role_authenticate(request):
    pk_logged_in = request.user.pk
    role_object = get_object_or_404(Role, id=pk_logged_in)
    role = role_object.role
    return role

def dashboard(request):
    role = role_authenticate(request)
    context = {
        'role': role,
        }
    return render(request, 'coordinator/dashboard.html', context)

def home(request):
    role = role_authenticate(request)
    context = {
        'role': role,
        }
    return render(request, 'index.html', context)

def add_profile_co(request):
    role = role_authenticate(request)
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
            messages.add_message(request, messages.SUCCESS, 'Coordinator information saved and needs activating!')
            print(form)
            print('test4')
        else:
            print(form.errors)
        return redirect('pending')
    context = {
        'form': form,
        'role': role,
        }
    return render(request, 'coordinator/add_profile.html', context)


def search_coordinators(request):
    role = role_authenticate(request)
    if request.method == "POST":
        searched = request.POST['search_co']
        co_profile_all=CoordinatorProfile.objects.filter(fname=searched).values()
        context = {
            'searched':searched,
            'co_profile_all':co_profile_all,
            'role': role,
        }
        return render(request, 'coordinator/choose_profile.html', context)
    else:
        return render(request, 'coordinator/choose_profile.html', {'role': role},)



def edit_profile_co(request, id):
    role = role_authenticate(request)
    co_profile_all=CoordinatorProfile.objects.filter().values() #gives the queryset with all details
    print(co_profile_all)
    co_profile = id #get_object_or_404(CoordinatorProfile, lname="one").id
    print(co_profile)
    profile = get_object_or_404(CoordinatorProfile, id=co_profile)
    if request.method == 'POST':
        form = ProfileFormCoUpdate(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Coordinator information updated!')
            return redirect('dashboard')
    form = ProfileFormCoUpdate(instance = profile)
    
    context = {
        'form': form,
        'profile': profile,
        'role': role,
    }
    return render(request, 'coordinator/update_profile.html', context)

def delete_profile_co(request, id):
    co_profile_all=CoordinatorProfile.objects.filter().values() #gives the queryset with all details
    print(co_profile_all)
    co_profile = id 
    print(co_profile)
    profile = get_object_or_404(CoordinatorProfile, id=co_profile)
    profile.delete()
    messages.add_message(request, messages.SUCCESS, 'Coordinator information deleted!')
    return redirect('dashboard')


def read_coordinator(request, id):
    role = role_authenticate(request)
    co_profile = id 
    profile = get_object_or_404(CoordinatorProfile, id=co_profile)
    coords = CharityProfile.objects.filter(charities_coordinators__id=co_profile)
    print(coords)
    context = {
        'profile': profile,
        'coords':coords,
        'role': role,
    }
    return render(request, 'coordinator/see_profile.html', context)

def get_verbose_name(name):
    session = VolunteerProfile._meta.get_field(name)
    verbose = session.verbose_name
    return verbose

def search_day_session(day_time):
    # Dynamically query using Q objects
    session_query = Q(**{f"{day_time}": True})
    session = VolunteerProfile.objects.filter(session_query)
    return session


def search_volunteer(request):
    role = role_authenticate(request)
    # get the list of activities to populate the dropdown select list
    activities = SkillChoices.objects.all().values()
    activity_list = []
    for activity in activities:
        name = activity.get('name')
        activity_list.append(name) 
    # when searching function below operates
    if request.method == "POST":
        activity_choice = request.POST.get("activity_choice") # user response to activity
        day_choice = request.POST.get("day_choice") # user response to day
        session_choice = request.POST.get("session_choice") # user response to session
        time = day_choice + session_choice # day and session in model field format
        volunteers_for_session = search_day_session(time)
        verbose_time = get_verbose_name(time)
        volunteers_for_activity = VolunteerProfile.objects.filter(skilled__name__icontains=activity_choice) # queryset filtered by activity user chose
        intersections = volunteers_for_activity & volunteers_for_session
        context = {
            'activity_list': activity_list,
            'activity_choice': activity_choice,
            'verbose_time': verbose_time,
            'intersections':intersections,
            'role':role,
            }
        return render(request, 'coordinator/search_volunteer.html', context)
    else:
        
        context = {
            'activity_list': activity_list,
            'role':role,
        }
        return render(request, 'coordinator/search_volunteer.html', context)
    
def activate_volunteers(request):
    role = role_authenticate(request)
    volunteers_for_activation = VolunteerProfile.objects.filter(activated=False)
    if request.method == "POST":
        print("volunteers_for_activation adjusted")
        context = {
            'volunteers_for_activation': volunteers_for_activation,
            'role': role,
        }
        return render(request, 'coordinator/activate_volunteer.html', context)
    else:
        context = {
            'volunteers_for_activation': volunteers_for_activation,
            'role': role,
        }
        return render(request, 'coordinator/activate_volunteers.html', context)
    
def activate_volunteer(request, id):
    role = role_authenticate(request)
    vol_id = id
    profile = get_object_or_404(VolunteerProfile, id=vol_id)
    skills = profile.skilled.values()
    peoples = VolunteerProfile.objects.filter(id=vol_id).values()
    true_pairs = [{key for key, value in people.items() if value is True} for people in peoples]
    sessions =[]
    for true_pair in true_pairs:
        for pair in true_pair:
            pair = get_verbose_name(pair)
            sessions.append(pair)
    if request.method == 'POST':
        form = ProfileFormVolunteer(request.POST, instance=profile)
        if form.is_valid():
            volunteer = form.save(commit=False)
            form.save()
            volunteer.save()
            messages.add_message(request, messages.SUCCESS, 'Charity information updated!')
            return redirect('activatevols')
    form = ProfileFormVolunteer(instance = profile)
    
    context = {
        'form': form,
        'profile': profile,
        'skills':skills,
        'sessions':sessions,
        'role': role
    }
    return render(request, 'coordinator/activate_volunteer.html', context)
    