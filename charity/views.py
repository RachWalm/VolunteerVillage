from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CharityProfile
from coordinator.models import CoordinatorProfile
from .forms import CharityForm
from role.models import Role


def role_authenticate(request):
    '''
    This function is part of the authentication process it gets the
    role information and whether the person has been activated to
    see if they are allowed access to the site returning their
    role if they might be allowed access which gives the next
    function the opportunity to decide to give access.
    '''
    pk_logged_in = request.user.pk  # who logged in
    role_object = get_object_or_404(Role, user_name_id=pk_logged_in)
    role = role_object.role  # gets integer associated with role
    profile = CoordinatorProfile.objects.filter(user_name_id=request.user.pk)
    activates = profile.values() # gets actual data from profile
    for activate in activates:
        active = activate['activated']  # if activated true
    if active:
        return role
    else:
        return 0  # block access


def home(request):
    '''Returns to landing page'''
    return render(request, 'index.html')


def add_charity(request):
    '''
    Allows a coordinator the form that will accept and put the information
    about the charity that they input into the data base.
    '''
    role = role_authenticate(request)  # only activated coordinators
    form = CharityForm
    if request.method == 'POST':
        form = CharityForm(request.POST)
        if form.is_valid():
            charity = form.save(commit=False)
            form.save()
            charity.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Charity information added')
    context = {
        'form': form,
        'role': role,
        }
    return render(request, 'charity/add_charity.html', context)


def search_charity(request):
    '''
    Provides a form and takes the data from the form into search for
    coordinators to search the charities part of the database. It then
    filters the the charities and returns the ones that match the input
    text in the charity name.
    This page will then let the read/edit/delete.
    '''
    role = role_authenticate(request)  # only activated coordinators
    if request.method == "POST":
        search = request.POST['search']
        profile = CharityProfile.objects.filter(charity_name__icontains=search)
        charity_profile_all = profile.values()
        content = charity_profile_all.exists()
        context = {
            'search': search,
            'charity_profile_all': charity_profile_all,
            'content': content,
            'role': role,
        }
        return render(request, 'charity/choose_charity.html', context)
    else:  # only activated coordinators
        context = {
            'role': role
        }
        return render(request, 'charity/choose_charity.html', context)


def read_charity(request, id):
    '''
    Allows the coordinator to look at information about the charity in an
    environment that they can't risk changing anything so just gather
    information.
    '''
    role = role_authenticate(request)  # only activated coordinators
    ch_profile = id
    profile = get_object_or_404(CharityProfile, id=ch_profile)
    coords = profile.charities_coordinators.values()
    context = {
        'profile': profile,
        'coords': coords,
        'role': role,
    }
    return render(request, 'charity/read_charity.html', context)


def edit_charity(request, id):
    '''
    Allows coordinators to add or change information that is stored
    about a charity, including name of charity, description and
    which coordinators are connected to the charity.
    '''
    role = role_authenticate(request)  # only activated coordinators
    ch_profile = id
    profile = get_object_or_404(CharityProfile, id=ch_profile)
    if request.method == 'POST':
        form = CharityForm(request.POST, instance=profile)
        if form.is_valid():
            charity = form.save(commit=False)
            form.save()
            charity.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Charity information updated!')
            return redirect('dashboard')
    form = CharityForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'role': role,
    }
    return render(request, 'charity/update_charity.html', context)


def delete_charity(request, id):
    '''
    This function is activated when a coordinator wants to delete a
    specific charity. It is activated from the modal that confirms
    the request to delete the charity.
    '''
    role = role_authenticate(request)
    if role == 2:  # only activated coordinators
        charity = get_object_or_404(CharityProfile, id=id)
        charity.delete()
        messages.add_message(request, messages.WARNING,
                             'Charity information deleted!')
        return redirect('dashboard')
    else:
        return redirect('index')
