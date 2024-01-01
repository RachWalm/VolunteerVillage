from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CharityProfile
from .forms import CharityForm


def home(request):
    return render(request, 'index.html')


def add_charity(request):
    form= CharityForm
    if request.method == 'POST':
        form = CharityForm(request.POST) 
        if form.is_valid(): 
            form.save()
        else:
            print(form.errors)
        return redirect('dashboard')
    context = {
        'form': form,
        }
    return render(request, 'charity/add_profile.html', context)

def search_charity(request):
    if request.method == "POST":
        searched = request.POST['search']
        charity_profile_all=CharityProfile.objects.filter(charity_name__icontains=searched).values()
        context = {
            'searched':searched,
            'charity_profile_all':charity_profile_all,
        }
        return render(request, 'charity/choose_charity.html', context)
    else:
        return render(request, 'charity/choose_charity.html',)


def read_charity(request, id):
    ch_profile = id #get_object_or_404(CoordinatorProfile, lname="one").id
    print(ch_profile)
    profile = get_object_or_404(CharityProfile, id=ch_profile)
    coords = profile.charities_coordinators.values()
    context = {
        # 'form': form,
        'profile': profile,
        'coords':coords,
        # 'pk_logged_in': pk_logged_in
    }
    return render(request, 'charity/read_charity.html', context)
    
    

def edit_charity(request, id):
    # pk_logged_in = request.user.pk
    # co_profile_all=CharityProfile.objects.filter().values() #gives the queryset with all details
    # print(co_profile_all)
    # which_coordinator(request)
    ch_profile = id #get_object_or_404(CoordinatorProfile, lname="one").id
    print(ch_profile)
    profile = get_object_or_404(CharityProfile, id=ch_profile)
    if request.method == 'POST':
        form = CharityForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = CharityForm(instance = profile)
    
    context = {
        'form': form,
        'profile': profile,
        # 'pk_logged_in': pk_logged_in
    }
    return render(request, 'charity/update_charity.html', context)

def delete_charity(request):
    pk_logged_in = request.user.pk
    user = get_object_or_404(User, id=pk_logged_in)
    user.delete()
    return redirect('dashboard')

# messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
