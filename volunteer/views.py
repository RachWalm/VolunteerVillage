from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import VolunteerProfile, Skills, DAYS_OF_WEEK, PART_OF_DAY, SkillChoices
from .forms import ProfileForm, SkillsForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def read_profile(request):
    pk_logged_in = request.user.pk
    people = VolunteerProfile.objects.filter(user_name_id=pk_logged_in).values()
    skills = Skills.objects.filter(user_name_id =pk_logged_in).values()
    true_pairs = [{key for key, value in available.items() if value is True} for available in people]
    context = {
        'people': people,
        'skills': skills,
        'pk_logged_in': pk_logged_in,
        'true_pairs': true_pairs
    }
    return render(request, 'volunteer/read_profile.html', context)

def add_profile(request):
    form= ProfileForm
    form2= SkillsForm
    if request.method == 'POST':
        form_data = {
            'user_name': request.user,
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'phone': request.POST['phone'], 
            'special_skills_description': request.POST['special_skills_description'],
            'user_name': request.user,
            'name': request.user,
            'time_length_days': request.POST['time_length_days'],
            'time_length_hours': request.POST['time_length_hours'],
            'mon_am': request.POST['mon_am'],
            'mon_pm': request.POST['mon_pm'],
            'mon_ev': request.POST['mon_ev'],
            'tue_am': request.POST['tue_am'],
            'tue_pm': request.POST['tue_pm'],
            'tue_ev': request.POST['tue_ev'],
            'wed_am': request.POST['wed_am'],
            'wed_pm': request.POST['wed_pm'],
            'wed_ev': request.POST['wed_ev'],
            'thu_am': request.POST['thu_am'],
            'thu_pm': request.POST['thu_pm'],
            'thu_ev': request.POST['thu_ev'],
            'fri_am': request.POST['fri_am'],
            'fri_pm': request.POST['fri_pm'],
            'fri_ev': request.POST['fri_ev'],
            'sat_am': request.POST['sat_am'], 
            'sat_pm': request.POST['sat_pm'],
            'sat_ev': request.POST['sat_ev'],
            'sun_am': request.POST['sun_am'],
            'sun_pm': request.POST['sun_pm'], 
            'sun_ev': request.POST['sun_ev'],
        }
        # form2_data = {
        #     'user_name': request.user,
        #     'name': request.user,
        #     'skilled': request.POST['skilled'],
        # }
        
        form = ProfileForm(form_data) 
        # form2 = SkillsForm(form2_data)
        # for field in form2:
        #     print("field Error:", field.name, field.errors)
        if form.is_valid(): # and form2.is_valid():
            print(form.is_valid)
            print(form2.is_valid)
            print('tesst5')
            profile = form.save(commit=False)
            profile.user_name = request.user
            profile.name = request.user
            form.save()
            print('test6')
            # ability = form2.save(commit=False)
            # # skill = form2.cleaned_data['skilled']
            # # print(skill)
            # # Skills.skilled.set(skill)
            # ability.user_name = request.user
            # print('test9')
            # ability.name = request.user
            # print('test10')
            # form2.save()
            # clean = form2.cleaned_data['skilled']
            # print('clean = ' + clean)
            # ability.skilled.set(clean)
            # # print('ability = ' + ability)
            # ability.save()
            # print('test13')
            # # print(str(ability.skilled))
            # # ability.skilled = skill
            # # ability.skilled.set(str(skill))
            # # print(ability.skilled.set(skill))
            # # # ability.save()
            # # ability.save()
            print('test7')
            # print(form)
            # print(form2)
            print('test4')
            messages.add_message(request, messages.SUCCESS, 'Profile sent for approval -  then you will be matched!')
        else:
            print('testelse')
            print(form.errors)
        return redirect('read')
    context = {
        'form': form,
        'form2': form2,
        }
    return render(request, 'volunteer/add_profile.html', context)



def edit_profile(request):
    pk_logged_in = request.user.pk
    people = get_object_or_404(VolunteerProfile, id=pk_logged_in)
    skilled = get_object_or_404(Skills, user_name_id =pk_logged_in)
    availabilities = get_object_or_404(VolunteerProfile, user_name_id =pk_logged_in)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=people)
        form2 = SkillsForm(request.POST, instance=skilled)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('read')
    form = ProfileForm(instance = people)
    form2 = SkillsForm(instance = skilled)
    context = {
        'form': form,
        'form2': form2,
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