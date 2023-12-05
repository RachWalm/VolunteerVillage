from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import VolunteerProfile, Skills, TimePeriod, DAYS_OF_WEEK, PART_OF_DAY
from .forms import ProfileForm, SkillsForm, TimeForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def read_profile(request):
    personlogged_in = User.username
    people = VolunteerProfile.objects.filter(user_name_id='1').values()
    skills = Skills.objects.filter(user_name_id ='1').values()
    availabilities = TimePeriod.objects.filter(user_name_id ='1').values()
    time = get_object_or_404(TimePeriod).day
    section = get_object_or_404(TimePeriod).section_of_day
    section_name = PART_OF_DAY[section][1]
    day_name = DAYS_OF_WEEK[time][1]
    context = {
        'people': people,
        'skills':skills,
        'availabilities': availabilities,
        'personlogged_in': personlogged_in,
        'day_name': day_name,
        'section_name': section_name
    }
    return render(request, 'volunteer/read_profile.html', context)


def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        form2 = SkillsForm(request.POST)
        form3 = TimeForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
        return redirect('read')
    form = ProfileForm()
    form2 = SkillsForm()
    form3 = TimeForm()
    context = {'form': form,
                'form2': form2,
                'form3': form3
                }
    return render(request, 'volunteer/add_profile.html', context)

# def edit_item(request, item_id):
#     item = get_object_or_404(VolunteerProfile, id=item_id)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('add_volunteer')
#     form = ProfileForm(instance=item)
#     context = {
#         'form': form
#     }
#     return render(request, 'volunteer/add_profile.html', context)