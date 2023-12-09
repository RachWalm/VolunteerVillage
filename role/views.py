from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Role
from .forms import RoleForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid() :
            form.save()
        # pk_logged_in = request.user.pk
        # titles = Role.objects.filter(user_name_id =pk_logged_in).values()
        # for title in titles:
        #     capability = title['role']
        #     if capability == 'Volunteer':
        return redirect('add')
            # elif capability == 'Coordinator':
            #     return redirect('pending')
            # else:
            #     return redirect('index')
    form = RoleForm()
    context = {'form': form,
                #'title':title,
                #'capability':capability
                }
    return render(request, 'role/role.html', context)