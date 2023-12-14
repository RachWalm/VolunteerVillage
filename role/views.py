from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Role
from volunteer.models import VolunteerProfile
from .forms import RoleForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def role(request):
    pk_logged_in = request.user.pk
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid() :
            form.save()
        title = Role.objects.filter(user_name_id =pk_logged_in).values()
        if title[0]['role'] == 1:
            return redirect('add')
        elif title[0]['role'] == 2:
            return redirect('pending')
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
    title = Role.objects.filter(user_name_id =pk_logged_in).values()
    VP_exists = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).exists()
    print(title[0]['role'])
    print(VP_exists)
    if title[0]['role'] == 1 and VP_exists:
        return redirect('read')
    elif title[0]['role'] == 1 and VP_exists == False:
        return redirect('add')
    elif title[0]['role'] == 2:
        return redirect('index') #will later take you to coordinator dashboard when set up
    else:
        return redirect('index')