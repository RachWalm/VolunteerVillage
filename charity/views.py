from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CharityProfile
from coordinator.models import CoordinatorProfile
from .forms import CharityForm
from role.models import Role


def role_authenticate(request):
    pk_logged_in = request.user.pk
    role_object = get_object_or_404(Role, user_name_id=pk_logged_in)
    role = role_object.role
    profile = CoordinatorProfile.objects.filter(user_name_id=request.user.pk)
    activates = profile.values()
    for activate in activates:
        active = activate['activated']
    if active:
        return role
    else:
        return 0


def home(request):
    return render(request, 'index.html')


def add_charity(request):
    role = role_authenticate(request)
    form = CharityForm
    if request.method == 'POST':
        form = CharityForm(request.POST)
        if form.is_valid():
            charity = form.save(commit=False)
            form.save()
            charity.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Charity information added')
        else:
            print(form.errors)
        return redirect('dashboard')
    context = {
        'form': form,
        'role': role,
        }
    return render(request, 'charity/add_charity.html', context)


def search_charity(request):
    role = role_authenticate(request)
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
    else:
        context = {
            'role': role
        }
        return render(request, 'charity/choose_charity.html', context)


def read_charity(request, id):
    role = role_authenticate(request)
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
    role = role_authenticate(request)
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
    role = role_authenticate(request)
    if role == 2:
        charity = get_object_or_404(CharityProfile, id=id)
        charity.delete()
        messages.add_message(request, messages.WARNING,
                             'Charity information deleted!')
        return redirect('dashboard')
    else:
        return redirect('index')
