from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CoordinatorProfile
from .forms import ProfileFormCo, ProfileFormCoUpdate, ChooseCo

# Create your views here.

def pending(request):
    return render(request, 'coordinator/pending.html')

def dashboard(request):
    # which_coordinator(request)
    return render(request, 'coordinator/dashboard.html')

def home(request):
    return render(request, 'index.html')

def add_profile_co(request):
    form= ProfileFormCo
    if request.method == 'POST':
        form_data_co = {
            'user_name': request.user,
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
        }

        print('test')
        form = ProfileFormCo(form_data_co) 
        print(form.is_valid)
        if form.is_valid(): 
            print('tesst5')
            profile = form.save(commit=False)
            profile.user_name = request.user
            form.save()
            print(form)
            print('test4')
        else:
            print(form.errors)
        return redirect('pending')
    context = {
        'form': form,
        }
    return render(request, 'coordinator/add_profile.html', context)


def choose_edit_co_profile(request):
    form=ChooseCo
    if request.method == 'POST':
        form_data_co = {
            'first': request.POST['first'],
            'last': request.POST['last'],
        }
        print('test')
        choose_form = ChooseCo(form_data_co) 
        queryset = CoordinatorProfile.objects.values_list()
        # post = get_object_or_404(queryset, slug=slug)
        # choose_form = ChooseCo(data=request.POST)
        if choose_form.is_valid():
            choose = choose_form.save(commit=False)
            choose.save()
        else:
            print(form.errors)
        return redirect('updateco')

    context = {
        'form': form,
        }
    return render(request, 'coordinator/dashboard.html', context)


# def which_coordinator(request):
#     print('witch')
    
#     form=ProfileFormCo
#     if request.method == 'POST':
#         form_data_co = {
#             'fname': request.POST['fname'],
#             'lname': request.POST['lname'],
#         }
#     form=ProfileFormCo(form_data_co)
#     if form.is_valid():
#         print('which')
#         # print(first_input)
#         # print(last_input)

    

def edit_profile_co(request):
    pk_logged_in = request.user.pk
    co_profile_all=CoordinatorProfile.objects.filter().values() #gives the queryset with all details
    print(co_profile_all)
    # which_coordinator(request)
    co_profile = get_object_or_404(CoordinatorProfile, lname="one").id
    print(co_profile)
    profile = get_object_or_404(CoordinatorProfile, id=co_profile)
    if request.method == 'POST':
        form = ProfileFormCoUpdate(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = ProfileFormCoUpdate(instance = profile)
    
    context = {
        'form': form,
        'profile': profile,
        'pk_logged_in': pk_logged_in
    }
    return render(request, 'coordinator/update_profile.html', context)

def delete_profile_co(request):
    pk_logged_in = request.user.pk
    user = get_object_or_404(User, id=pk_logged_in)
    user.delete()
    return redirect('dashboard')

# messages.add_message(request, messages.SUCCESS, 'Comment deleted!')