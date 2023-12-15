from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Role
from volunteer.models import VolunteerProfile
from coordinator.models import CoordinatorProfile
from .forms import RoleForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def role(request):
    form = RoleForm
    pk_logged_in = request.user.pk
    if request.method == 'POST':
        form_data_role = {
            'user_name': request.user,
            'name': request.user,
            'role': request.POST['role'],
        }
        form = RoleForm(form_data_role)
        if form.is_valid() :
            role=form.save(commit=False)
            role.user_name = request.user
            role.name = request.user
            form.save()
        title = Role.objects.filter(user_name_id =pk_logged_in).values()
        if title[0]['role'] == 1:
            return redirect('add')
        elif title[0]['role'] == 2:
            return redirect('addco')
        else:
            return redirect('index')
    form = RoleForm()
    context = {'form': form,}
    return render(request, 'role/role.html', context)

def login_success(request):
    """
    Redirects users based on the role that the need to use the site
    """
    pk_logged_in = request.user.pk
    role_exists = Role.objects.filter(user_name_id=pk_logged_in).exists()
    if role_exists:
        title = Role.objects.filter(user_name_id =pk_logged_in).values()
        VP_exists = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).exists()
        CP_exists = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in).exists()
        co_profile = CoordinatorProfile.objects.filter(user_name_id =pk_logged_in).values()
        print(co_profile[0]['activated'])
        print(title[0]['role'])
        print(VP_exists)
        print(CP_exists)
        if title[0]['role'] == 1 and VP_exists:
            return redirect('read')
        elif title[0]['role'] == 1 and VP_exists == False:
            return redirect('add')
        elif title[0]['role'] == 2 and CP_exists == False:
            return redirect('addco') #will later take you to coordinator dashboard when set up
        elif title[0]['role'] == 2 and CP_exists:
            if co_profile[0]['activated']:
                return redirect('dashboard')
            elif co_profile[0]['activated'] == False:
                return redirect('pending')
            else:
                return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('role')