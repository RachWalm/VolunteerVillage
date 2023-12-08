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
        return redirect('add')
    form = RoleForm()
    context = {'form': form,
                }
    return render(request, 'role/role.html', context)