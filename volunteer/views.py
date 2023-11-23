from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import VolunteerProfile
from .forms import ProfileForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def read_profile(request):
    profile = VolunteerProfile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'volunteer/add_profile.html', context)

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('add_profile')
    form = ProfileForm()
    context = {'form': form}
    return render(request, 'volunteer/add_profile.html', context)