from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import VolunteerProfile, Skills, TimePeriod, DAYS_OF_WEEK, PART_OF_DAY, SkillChoices
from .forms import ProfileForm, SkillsForm, TimeForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def read_profile(request):
    # user = get_object_or_404(User, id=pk) NEED TO LOOK AT WHICH VARIABLES STILL NEEDED ON PAGE
    pk_logged_in = request.user.pk
    people = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).values()
    skills = Skills.objects.filter(user_name_id =pk_logged_in).values()
    availabilities = TimePeriod.objects.filter(user_name_id =pk_logged_in).values()
    for available in availabilities:
        time = available['day']
        section = available['section_of_day']
    for skill in skills:
        able = skill['skilled']
    section_name = PART_OF_DAY[section][1]
    day_name = DAYS_OF_WEEK[time][1]
    skill_name = SkillChoices.SKILL_CHOICES[able-1][1] # first is corresponding number -1
    context = {
        'people': people,
        'skills': skills,
        'availabilities': availabilities,
        'pk_logged_in': pk_logged_in,
        'day_name': day_name,
        'section_name': section_name,
        'skill_name':skill_name,
        'time':time,
        'able':able,
        'section':section,
    }
    return render(request, 'volunteer/read_profile.html', context)

def add_profile(request):
    form= ProfileForm
    form2= SkillsForm
    form3=TimeForm
    if request.method == 'POST':
        form_data = {
            'user_name': request.user,
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'phone': request.POST['phone'], 
            'profile_picture': request.POST['profile_picture'], 
            'special_skills_description': request.POST['special_skills_description'],
        }
        form2_data = {
            'user_name': request.user,
            'name': request.user,
            'skilled': request.POST['skilled'],
        }
        form3_data = {
            'user_name': request.user,
            'name': request.user,
            'time_length_days': request.POST['time_length_days'],
            'time_length_hours': request.POST['time_length_hours'],
            'section_of_day': request.POST['section_of_day'],
            'day': request.POST['day'],
        }

        print('test')
        form = ProfileForm(form_data) 
        form2 = SkillsForm(form2_data)
        form3 = TimeForm(form3_data)
        print(form.is_valid)
        print(form2.is_valid)
        print(form2.is_valid)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            print('tesst5')
            profile = form.save(commit=False)
            profile.user_name = request.user
            form.save()
            print('test6')
            ability = form2.save(commit=False)
            print('test8')
            ability.user_name = request.user
            print('test9')
            ability.name = request.user
            print('test10')
            form2.save()
            print('test7')
            time = form3.save(commit=False)
            time.user_name = request.user
            time.name = request.user
            form3.save()
            print(form)
            print(form2)
            print(form3)
            print('test4')
            messages.add_message(request, messages.SUCCESS, 'Profile sent for approval -  then you will be matched!')
        else:
            print(form.errors)
        return redirect('index')
    context = {
        'form': form,
        # 'form':ProfileForm(),
        'form2': form2,
        'form3': form3,
        # 'pk_logged_in': pk_logged_in,
        }
    return render(request, 'volunteer/add_profile.html', context)



def edit_profile(request):
    pk_logged_in = request.user.pk
    people = get_object_or_404(VolunteerProfile, id=pk_logged_in)
    skilled = get_object_or_404(Skills, user_name_id =pk_logged_in)
    availabilities = get_object_or_404(TimePeriod, user_name_id =pk_logged_in)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=people)
        form2 = SkillsForm(request.POST, instance=skilled)
        form3 = TimeForm(request.POST, instance=availabilities)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            return redirect('read')
    form = ProfileForm(instance = people)
    form2 = SkillsForm(instance = skilled)
    form3 = TimeForm(instance = availabilities)
    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'people': people,
        'skilled': skilled,
        'availabilities': availabilities,
        'pk_logged_in': pk_logged_in
    }
    return render(request, 'volunteer/edit_profile.html', context)

def delete_profile(request):
    pk_logged_in = request.user.pk
    user = get_object_or_404(User, id=pk_logged_in)
    user.delete()
    return redirect('index')

# messages.add_message(request, messages.SUCCESS, 'Comment deleted!')