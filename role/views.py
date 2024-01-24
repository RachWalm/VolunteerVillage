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
    if request.method == 'POST':
        form_data_role = {
            'user_name': request.user, #links to the allauth model
            'name': request.user, # needed so that we can have a human readable string returned
            'role': request.POST['role'], # takes entered value
        }
        form = RoleForm(form_data_role)
        if form.is_valid() :
            role=form.save(commit=False)
            role.user_name = request.user #links to the allauth model
            role.name = request.user # needed so that we can have a human readable string returned
            form.save()
            messages.add_message(request, messages.INFO, 'Your role has been assigned')
        # below sends the user to the correct next stage of sign up
        title = Role.objects.filter(user_name_id =pk_logged_in).values()
        if title[0]['role'] == 1:
            return redirect('add') # chose volunteer so goes to volunteer add page
        elif title[0]['role'] == 2:
            return redirect('addco') # chose coordinator so goes to coordinator profile page
        else:
            return redirect('index') # just in case
    form = RoleForm()
    context = {'form': form,}
    return render(request, 'role/role.html', context)


def login_success(request):
    """
    Redirects users based on the role that the need to use the site
    """
    pk_logged_in = request.user.pk
    role_exists = Role.objects.filter(user_name_id=pk_logged_in).exists()
    if role_exists: # role is chosen
        title = Role.objects.filter(user_name_id =pk_logged_in).values() # sees whether they signed up as volunteer 1 or coordinator 2
        VP_exists = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).exists() #checks if they have a profile stored
        CP_exists = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in).exists() # checks if they have a profile stored
        co_profile = CoordinatorProfile.objects.filter(user_name_id =pk_logged_in).values() # gets profile so can check if activated
        if title[0]['role'] == 1 and VP_exists: # volunteer with profile
            return redirect('read') # see volunteer profile
        elif title[0]['role'] == 1 and VP_exists == False: # volunteer without profile
            return redirect('add') # form to fill out volunteer profile
        elif title[0]['role'] == 2 and CP_exists == False: # coordinator without a profile
            return redirect('addco') # form to fill out coordinator profile
        elif title[0]['role'] == 2 and CP_exists: # coordinator with a profile
            if co_profile[0]['activated']: # coordinator with a profile and activated
                return redirect('dashboard')
            elif co_profile[0]['activated'] == False: # unactivated coordinator so no access
                return redirect('pending')
            else:
                return redirect('index') # just in case
        else:
            return redirect('index') # just in case
    else:
        return redirect('role') # hasn't chosen role yet
    