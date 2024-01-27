from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import CoordinatorProfile
from volunteer.models import VolunteerProfile, SkillChoices
from role.models import Role
from charity.models import CharityProfile
from .forms import ProfileFormCo, ProfileFormCoUpdate, ProfileFormVolunteer


def pending(request):
    '''A page that while the coordinator hasn't been activated they are
    directed to. Avoids access for spam profiles.
    '''
    profile = CoordinatorProfile.objects.filter(user_name_id=request.user.pk)
    activates_coordinator = profile.values()  # get data associated
    for activate_coordinator in activates_coordinator:
        active = activate_coordinator['activated']
    context = {
        'active': active,
        }
    return render(request, 'coordinator/pending.html', context)


def role_authenticate(request):
    '''
    This function is part of the authentication process it gets the
    role information and whether the person has been activated to
    see if they are allowed access to the site returning their
    role if they might be allowed access which gives the next
    function the opportunity to decide to give access.
    '''
    pk_logged_in = request.user.pk  # logged in user
    role_object = get_object_or_404(Role, user_name_id=pk_logged_in)
    role = role_object.role  # gets integer associated with role
    profile = CoordinatorProfile.objects.filter(user_name_id=request.user.pk)
    activates_coordinator = profile.values()  # get data associated
    for activate_coordinator in activates_coordinator:
        active = activate_coordinator['activated']
    if active:
        return role
    else:
        return 0


def dashboard(request):
    '''
    Provides number of coordinators not activated and their names.
    Provides number of volunteers not activated. Provides buttons
    to perform all the actions a coordinator role would want to
    perform
    '''
    role = role_authenticate(request)  # activated coordinator only
    co_not_activated = CoordinatorProfile.objects.filter(activated=False)
    co_not_activated_count = co_not_activated.count()
    vol_not = VolunteerProfile.objects.filter(activated=False)
    vol_not_activated = vol_not.count()
    context = {
        'role': role,
        'co_not_activated': co_not_activated,
        'co_not_activated_count': co_not_activated_count,
        'vol_not_activated': vol_not_activated,
        }
    return render(request, 'coordinator/dashboard.html', context)


def home(request):
    '''Allows access to home page'''
    return render(request, 'index.html')


def add_profile_co(request):
    '''
    Checks if the coordinator already has a profile so it doesn't
    attempt to produce another one. Provides a form to allow the
    coordinator to add their name, ready for activation with a
    setup profile.
    '''
    pk_logged_in = request.user.pk  # activated coordinator only
    cp = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in)
    CP_exists = cp.exists()
    form = ProfileFormCo
    if request.method == 'POST':
        form_data_co = {
            'user_name': request.user,
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
        }
        form = ProfileFormCo(form_data_co)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_name = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Profile saved and needs activating!')
        return redirect('pending')
    context = {
        'form': form,
        'CP_exists': CP_exists,
        }
    return render(request, 'coordinator/add_profile.html', context)


def search_coordinators(request):
    '''
    This takes a text value from a input on a form and looks for any
    coordinator profile with an fname that contains that value. It
    should be able to cope with either capitals or little letters
    due to icontains.
    Returns the values of the profiles that match.
    '''
    role = role_authenticate(request)  # activated coordinator only
    if request.method == "POST":
        searched = request.POST['search_co']
        profile = CoordinatorProfile.objects.filter(fname__icontains=searched)
        found = profile.count()
        co_profile_all = profile.values()
        context = {
            'searched': searched,
            'co_profile_all': co_profile_all,
            'role': role,
            'found': found,
            }
        return render(request, 'coordinator/choose_profile.html', context)
    else:
        return render(request, 'coordinator/choose_profile.html',
                      {'role': role},)


def edit_profile_co(request, id):
    '''
    This gathers the information on the coordinator that has the id
    provided alongside the request in the arguments and prepopulates
    a form so that the coordinator can look at their own or other
    coordinators profiles and change them or activate or deactivate
    the profile as required.
    '''
    role = role_authenticate(request)  # activated coordinators only
    co_profile = id
    profile = get_object_or_404(CoordinatorProfile, id=co_profile)
    if request.method == 'POST':
        form = ProfileFormCoUpdate(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Coordinator information updated!')
            return redirect('dashboard')
    form = ProfileFormCoUpdate(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'role': role,
    }
    return render(request, 'coordinator/update_profile.html', context)


def delete_profile_co(request, id):
    '''
    This gathers the information on the coordinator that has the id
    provided alongside the request in the arguments and from the
    modal that confirms that the coordinator profile should be
    deleted it performs a delete of the profile (not the user).
    '''
    role = role_authenticate(request)  # activated coordinators only
    if role == 2:
        co_profile = id
        profile = get_object_or_404(CoordinatorProfile, id=co_profile)
        profile.delete()
        messages.add_message(request, messages.WARNING,
                             'Coordinator information deleted!')
        return redirect('index')
    else:
        return redirect('index')


def read_coordinator(request, id):
    '''
    This gathers the information on the coordinator that has the id
    provided alongside the request in the arguments and give a
    non-interactive version of the coordinator profile so that
    it can't be mistakenly edited.
    '''
    try:
        role = role_authenticate(request)
        co = id
        profile = get_object_or_404(CoordinatorProfile, id=co)
        coords = CharityProfile.objects.filter(charities_coordinators__id=co)
        context = {
            'profile': profile,
            'coords': coords,
            'role': role,
        }
        return render(request, 'coordinator/see_profile.html', context)
    except AttributeError:
        error_message = "No charities, add them to a charity and return"
        context = {
            'error_message': error_message
        }
        return render(request, 'coordinator/see_profile.html', context)


def get_verbose_name(name):
    '''
    As some of the field names aren't easy for users to interpret this
    collects the verbose name which is a version that is user friendly
    to be displayed on the page.
    '''
    session = VolunteerProfile._meta.get_field(name)
    verbose = session.verbose_name
    return verbose


def search_day_session(day_time):
    '''
    This is the volunteer search that is performed which takes a
    field name which is generated in search volunteers from two
    input fields and returning only profiles that have true in
    that field via a filter.
    '''
    # Dynamically query using Q objects
    session_query = Q(**{f"{day_time}": True})  # true value for session
    session = VolunteerProfile.objects.filter(session_query)
    return session


def search_volunteer(request):
    '''
    This firstly populates one input from options of activities
    stored in the database, then takes values from three selects
    which provide the activity, day and part of day. Day and part
    of day are then combined to give a field name which is
    searched by search_day_session and values that match the
    search for activity and day/session are then returned so that
    a coordinator can contact them outside the database from their
    details.
    '''
    role = role_authenticate(request)  # only activated coordinators
    # get the list of activities to populate the dropdown select list
    activities = SkillChoices.objects.all().values()
    activity_list = []
    for activity in activities:
        name = activity.get('name')
        activity_list.append(name)
    # when searching function below operates
    if request.method == "POST":
        # user response to activity
        activity_choice = request.POST.get("activity_choice")
        # user response to day
        day_choice = request.POST.get("day_choice")
        # user response to session
        session_choice = request.POST.get("session_choice")
        # day and session in model field format
        time = day_choice + session_choice
        volunteers_for_session = search_day_session(time)
        verbose_time = get_verbose_name(time)
        # queryset filtered by activity user chose
        ac = VolunteerProfile.objects.all()
        act = ac.filter(skilled__name__icontains=activity_choice)
        intersections = act & volunteers_for_session
        context = {
            'activity_list': activity_list,
            'activity_choice': activity_choice,
            'verbose_time': verbose_time,
            'intersections': intersections,
            'role': role,
            }
        return render(request, 'coordinator/search_volunteer.html', context)
    else:
        context = {
            'activity_list': activity_list,
            'role': role,
        }
        return render(request, 'coordinator/search_volunteer.html', context)


def activate_volunteers(request):
    '''
    This filters out all the volunteers that aren't activated yet so that
    they can be examined for spam profiles or current needs into a list.
    Each one can be clicked on and activated on next page.
    '''
    role = role_authenticate(request)  # activated coordinators only
    activation = VolunteerProfile.objects.filter(activated=False)
    if request.method == "POST":
        context = {
            'volunteers_for_activation': activation,
            'role': role,
        }
        return render(request, 'coordinator/activate_volunteer.html', context)
    else:
        context = {
            'volunteers_for_activation': activation,
            'role': role,
        }
        return render(request, 'coordinator/activate_volunteers.html', context)


def activate_volunteer(request, id):
    '''
    Coordinators get all the details in a non-editable view so that they can
    examine them without risk of editing and if they want them in the
    database they can activate them, or report spam profiles to the superuser.
    By going through them they can identify people they are adding to the
    database that there is already a current need.
    '''
    role = role_authenticate(request)  # activated coordinators only
    vol_id = id
    profile = get_object_or_404(VolunteerProfile, id=vol_id)
    skills = profile.skilled.values()
    peoples = VolunteerProfile.objects.filter(id=vol_id).values()
    true_pairs = [{key for key, value in people.items() if value is True}
                  for people in peoples]
    sessions = []
    for true_pair in true_pairs:
        for pair in true_pair:
            pair = get_verbose_name(pair)
            sessions.append(pair)
    if request.method == 'POST':
        form = ProfileFormVolunteer(request.POST, instance=profile)
        if form.is_valid():
            volunteer = form.save(commit=False)
            form.save()
            volunteer.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Volunteer activated!')
            return redirect('activatevols')
    form = ProfileFormVolunteer(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'skills': skills,
        'sessions': sessions,
        'role': role
    }
    return render(request, 'coordinator/activate_volunteer.html', context)
