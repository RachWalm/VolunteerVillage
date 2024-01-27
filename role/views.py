from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Role
from volunteer.models import VolunteerProfile
from coordinator.models import CoordinatorProfile
from .forms import RoleForm


def home(request):
    return render(request, 'index.html')


def role(request):
    form = RoleForm
    pk_logged_in = request.user.pk
    role_exists = Role.objects.filter(user_name_id=pk_logged_in).exists()
    if request.method == 'POST':
        form_data_role = {
            'user_name': request.user,  # links to the allauth model
            # needed so that we can have a human readable string returned
            'name': request.user,
            'role': request.POST['role'],  # takes entered value
        }
        form = RoleForm(form_data_role)
        if form.is_valid():
            role = form.save(commit=False)
            role.user_name = request.user  # links to the allauth model
            # needed so that we can have a human readable string returned
            role.name = request.user
            form.save()
            messages.add_message(request, messages.INFO,
                                 'Your role has been assigned')
        # below sends the user to the correct next stage of sign up
        title = Role.objects.filter(user_name_id=pk_logged_in).values()
        if title[0]['role'] == 1:
            # chose volunteer so goes to volunteer add page
            return redirect('add')
        elif title[0]['role'] == 2:
            # chose coordinator so goes to coordinator profile page
            return redirect('addco')
        else:
            return redirect('index')  # just in case
    form = RoleForm()
    context = {
        'form': form,
        'role_exists': role_exists,
        }
    return render(request, 'role/role.html', context)


def login_success(request):
    """
    Redirects users based on the role that the need to use the site
    """
    pk_logged_in = request.user.pk
    role_exists = Role.objects.filter(user_name_id=pk_logged_in).exists()
    if role_exists:  # role is chosen
        # sees whether they signed up as volunteer 1 or coordinator 2
        title = Role.objects.filter(user_name_id=pk_logged_in).values()
        # checks if they have a profile stored
        vp = VolunteerProfile.objects.filter(user_name_id=pk_logged_in)
        VP_exists = vp.exists()
        # checks if they have a profile stored
        cp = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in)
        CP_exists = cp.exists()
        # gets profile so can check if activated
        co = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in)
        co_profile = co.values()
        # volunteer with profile
        if title[0]['role'] == 1 and VP_exists:
            # see volunteer profile
            return redirect('read')
        # volunteer without profile
        elif title[0]['role'] == 1 and VP_exists is False:
            # form to fill out volunteer profile
            return redirect('add')
        # coordinator without a profile
        elif title[0]['role'] == 2 and CP_exists is False:
            return redirect('addco')  # form to fill out coordinator profile
        elif title[0]['role'] == 2 and CP_exists:  # coordinator with a profile
            # coordinator with a profile and activated
            if co_profile[0]['activated']:
                return redirect('dashboard')
            # unactivated coordinator so no access
            elif co_profile[0]['activated'] is False:
                return redirect('pending')
            else:
                return redirect('index')  # just in case
        else:
            return redirect('index')  # just in case
    else:
        return redirect('role')  # hasn't chosen role yet
