from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CoordinatorProfile
from .forms import ProfileFormCo, ProfileFormCoUpdate
from role.models import Role

# Create your views here.

def pending(request):
    return render(request, 'coordinator/pending.html')

def dashboard(request):
    pk_logged_in = request.user.pk
    role = get_object_or_404(Role, id=pk_logged_in)
    context = {
        'role': role,
        }
    return render(request, 'coordinator/dashboard.html', context)

def home(request):
    return render(request, 'index.html')

def add_profile_co(request):
    pk_logged_in = request.user.pk
    role = get_object_or_404(Role, id=pk_logged_in)
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
    pk_logged_in = request.user.pk
    role = get_object_or_404(Role, id=pk_logged_in)
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
    pk_logged_in = request.user.pk
    role = get_object_or_404(Role, id=pk_logged_in)
    co_profile_all=CoordinatorProfile.objects.filter().values() #gives the queryset with all details
    print(co_profile_all)
    # which_coordinator(request)
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
        'pk_logged_in': pk_logged_in,
        'role': role,
    }
    return render(request, 'coordinator/update_profile.html', context)

def delete_profile_co(request, id):
    # pk_logged_in = request.user.pk
    coordinator = get_object_or_404(CoordinatorProfile, id=id)
    coordinator.delete()
    messages.add_message(request, messages.SUCCESS, 'Coordinator information deleted!')
    return redirect('dashboard')


def read_coordinator(request, id):
    pk_logged_in = request.user.pk
    role = get_object_or_404(Role, id=pk_logged_in)
    co_profile = id #get_object_or_404(CoordinatorProfile, lname="one").id
    print(co_profile)
    profile = get_object_or_404(CoordinatorProfile, id=co_profile)
    coords = profile.coordinators_charities.values()
    print(coords)
    context = {
        # 'form': form,
        'profile': profile,
        'coords':coords,
        'role': role,
        # 'pk_logged_in': pk_logged_in
    }
    return render(request, 'coordinator/see_profile.html', context)