# Testing

## Validators

See README for validator information

### HTML validation

The HTML validation is below in a pdf.

[html validation](document/html.pdf)

### CSS validation

Code was manually copied to the validator.

![CSS validation](document/css.png)

### Javascript Validation

Code was manually copied to the validator.

[Coordinator add profile validation](document/covalidation.png)


[Volunteer add profile validation](document/volvalidation.png)


[delete charity check](document/deletecharity.png)


[delete coordinator check](document/deletecoordinator.png)


[delete volunteer check](document/deletevolunteer.png)


### Python Validation

Python code copy and pasted into validator and put in the pdf below.

[python validation](document/py.pdf)

## Lighthouse and accessibility

[index](document/lightindex.png) - performance could be improved with pictures resized and reformatted - this would be a future improvement.

### Allauth

[signup](document/lightsignup.png)

[login](document/lightlogin.png)

[logout](document/lightlogout.png)

### Charity

[add_charity](document/lightadd-charity.png)

[choose_charity](document/lightchoose-charity.png)

[read_charity](document/lightread-charity.png)

[update_charity](document/lightupdate-charity.png)

### Coordinator

[activate_volunteer](document/lightactivate-volunteers.png)

[activate_volunteers](document/lightactivate-volunteer.png)

[add_profile](document/lightcoadd-profile.png)

[choose_profile](document/lightchoose-profile.png)

[dashboard](document/lightdash.png)

[pending](document/lightpending.png)

[search_volunteers](document/lightsearch-volunteer.png)

[see_profile](document/lightsee-profile.png)

[update_profile](document/lightupdate-profile.png)

### Errors

[404](document/404.png)

[500](document/light500.png)

### Role

[role](document/lightrole.png)

### Volunteer

[add_profile](document/lightadd-profile.png)

[edit_profile](document/lightvoledit-profile.png)

[read_profile](document/lightvolread-profile.png)

## Features testing - Manual

Each page is tested for it's functionality for all features including python and JS functions. Features that appear in many pages maybe tested just once and referenced.

### Pages

All pages were checked that they went to the next logical one which was simple for all apart from log in. Log in used login_success to direct people according to role and what stage they are at. Here is the function and testing:

```
def login_success(request):
    """
    Redirects users based on the role and what stage of the sign up
    process they have completed to area they need to use the site.
    """
    pk_logged_in = request.user.pk
    role_exists = Role.objects.filter(user_name_id=pk_logged_in).exists()
    if role_exists:  # role is chosen
        # sees whether they signed up as volunteer 1 or coordinator 2
        title = Role.objects.filter(user_name_id=pk_logged_in).values()
        # checks if they have a profile stored
        vp = VolunteerProfile.objects.filter(user_name_id=pk_logged_in)
        VP_exists = vp.exists()
        # checks if they have a profile stored
        cp = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in)
        CP_exists = cp.exists()
        # gets profile so can check if activated
        co = CoordinatorProfile.objects.filter(user_name_id=pk_logged_in)
        co_profile = co.values()
        # volunteer with profile
        if title[0]['role'] == 1 and VP_exists:
            # see volunteer profile
            return redirect('read')
        # volunteer without profile
        elif title[0]['role'] == 1 and VP_exists is False:
            # form to fill out volunteer profile
            return redirect('add')
        # coordinator without a profile
        elif title[0]['role'] == 2 and CP_exists is False:
            return redirect('addco')  # form to fill out coordinator profile
        elif title[0]['role'] == 2 and CP_exists:  # coordinator with a profile
            # coordinator with a profile and activated
            if co_profile[0]['activated']:
                return redirect('dashboard')
            # unactivated coordinator so no access
            elif co_profile[0]['activated'] is False:
                return redirect('pending')
            else:
                return redirect('index')  # just in case
        else:
            return redirect('index')  # just in case
    else:
        return redirect('role')  # hasn't chosen role yet

```

- if not signed up it won't let you log in - Yes
- if no role exists should return role - Yes
- if role exists as volunteer and a volunteer profile exists return read - Yes
- if role exists as volunteer but no volunteer profile exists return add - Yes
- if role exists as coordinator but no coordinator profile exists return addco - Yes
- if role exists as coordinator with a coordinator profile who is activated return dashboard - Yes
- if role exists as coordinator with a coordinator profile who isn't activated return pending - Yes

This covers all the senarios I can imagine but if something doesn't follow that then it should redirect to index, but I am not sure how to force that.


#### Base.html on every page

Unless stated, base.html tested on index page, but visual check on every page - will be noted if doesn't work on any page tried.

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Looks correct on load|Page loaded as expected|Yes||
|Logo|Present and sized correctly|Yes||
|Favicon|Present|Yes||
|Appropriate message gap|visible items on each end with central gap|Yes||
|Sign in|Button looks right and leads to sign in when clicked|Yes||
|Sign up|Button looks right and leads to sign up when clicked|Yes||
|Home page link present|tested on many pages to return to home page and looks right|Yes||
|Website name|Name present in correct position|Yes||
|Content|Content inbetween base html|Yes||
|Footer|Correct colour and stuck to bottom with scrolling|Yes||
|Footer|Contains correct content and doesn't cover main page content|Yes||
|Signed in|When signed in sign up/in not present and who is signed in replaces it|Yes||
|Signed in|When signed in Nav on top right adds sign out and your homepage links tested on many pages|Yes||
|Signed in|sign out link works tested on many pages|Yes||
|Signed |Your home page link works tested on many pages|Yes||


#### Index page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|base.html|All base in place|Yes||
|Text and pictures|All in expected positions|Yes||
|Pictures|Aren't distorted on an views|Yes||
|Text|Adjust number of lines to fit view|Yes||
|Responsive|Changes to one column at suitable break point|Yes||
|||||

#### Sign up page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Page layout|Looks as expected|Yes||
|Form|Required boxes in place|Yes||
|Form|Can't sign up without a user name|Yes|Built in warning|
|Form|Can't sign up without password|Yes|Built in warning|
|Form|Can't leave second password blank|Yes|Built in warning|
|Form|Can't use password that doesn't meet criteria|Yes|Built in warning|
|Form|Can sign up with a e-mail address|Yes||
|Form|Can sign up without an e-mail address|Yes|optional in settings|
|Form|E-mail address must contain @|Yes||
|Form|E-mail address has to have format of email a@b.c|Yes||
|Form|Submit saves user|Yes||
|message|message at top of page for 2.5 seconds when sign up success|Yes||


#### Log in page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|layout|Looks as expected|Yes||
|inputs|Must enter a user name|Yes|Built in warning|
|inputs|Must enter a password|Yes||
|inputs|Not recognised username|Yes|Built in message|
|inputs|Not recognised password|Yes|Built in message|
|inputs|forgotten password link not available|Yes||
|sign in button|if everything is correct signs you in|Yes||
|message|message at top of page for 2.5 seconds when log in|Yes||

#### Log out page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|layout|Looks as expected|Yes||
|Sign out button|works as expected|Yes||
|message|message at top of page for 2.5 seconds when log out success|Yes||

#### Role choice page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Page layout|Looks as expected|Yes||
|Volunteer|sign up as volunteer select|Yes||
|Coordinator|Sign up as coordinator select|Yes||
|Multiple|Can't sign up as both|Yes||
|Submit volunteer|submitting saves as volunteer|Yes||
|Submit coordinator|submitting saves as coordinator|Yes||
|message|generates update message at top of screen for 2.5 seconds when saved|Yes||

#### Coordinator add profile

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|layout|looks as expected|Yes||
|form|Contains required inputs|Yes||
|form|Can't leave first name blank|Yes||
|form|Can't leave second name blank|Yes||
|form|Can't enter anything that isn't an name|No|See bugs|
|Submit|saves the data and moves you to pending page|Yes||
|message|generates update message at top of screen for 2.5 seconds when saved|Yes||


#### Pending activation page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|Looks as expected|Yes||
|Layout|no button to proceed in unactivated users|Yes||
|Layout|If user activated while still on page they can refresh to see button to proceed|Yes||
|Proceed button|Proceed button works|Yes||
|back button|if logged in an press back button it takes you to page|Yes||
|back button|if logged out no access|No access|Error 500|
|url|will take you there if logged in to correct version vs activated|Yes||
|url|will not work if not logged in|No access|Error 500|

#### Volunteer add profile page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Page title|Create your profile|Yes||
|Form|Contains expected boxes|Yes||
|Form|Clear which data and labels match|Yes||
|Form|Helper text stands out|Yes||
|Form|Verbose names making it human readable|Yes||
|Form Layout|As expected|Yes||
|Submit button|Saves new profile data|Yes||
|Page layout|As expected|Yes||
|JS validation|Alert works when first name empty|Yes||
|JS validation|Alert works when last name empty|Yes||
|JS validation|Alert works for letters or number not being 11 digits for the phone number|Yes||
|JS validation|Alert works if no skill is selected|Yes||
|JS validation|Alert work if hours per week negative|Yes||
|Form content|hours per week won't accept letters etc.|Yes||
|Form content|hours per week accepts 0|Yes||
|JS validation|Alert works if hours per week exceeds hours in a week|Yes||
|Form content|Accepts positive number in hours per week (with above exclusions)|Yes||
|JS validation|Alert work is days per week negative|Yes||
|Form content|days per week won't accept letters etc.|Yes||
|Form content|days per week accepts 0|Yes||
|JS validation|Alert works if days per week exceeds hours in a week|Yes||
|Form content|Accepts positive number in days per week (with above exclusions)|Yes||
|Form content|Will allow every timeslot to be accepted and save|Yes||
|Form content|Will allow random selection of timeslots to be accepted and save|Yes||
|Form content|Will allow no timeslots to be selected and save|Yes||
|Form content|Will allow one timeslot to be selected and save|Yes||
|Form content|Will allow text in the skills description box and save|Yes||
|Form content|Will allow no text in the skills description box and save|Yes||
|Form content|Will allow one skill selection to save|Yes||
|Form content|Will allow all skills selected to save|Yes||
|Form content|Will allow random selection of skills to save|Yes||
|Url|Can enter form using url if logged in|Yes|Not if you already have a profile|
|Url|Can't enter form using url if not logged in|No entry|404 error page|
|back button|Can enter and use form via back button if logged in|Yes||
|back button|Can't enter form by back button if not logged in|No entry|Just sends you to a blank page so can't adjust data but still nav links to get back|
|back button|No form if you already havve a profile and press back to add profile so can't confuse data|Yes|Warning and redirect|
|message|generates update message at top of screen for 2.5 seconds when saved|Yes||

#### Volunteer read their profile page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Nav links|Top left and lead to home page and edit profile respectively|Yes||
|Page title|Your profile and the user name|Yes||
|Table|Contains expected information|Yes||
|Table|Contents checked against admin version of that profile|Yes||
|Table|Clear which data and labels match|Yes||
|Table|Verbose names making it human readable|Yes||
|Table Layout|As expected|Yes||
|Edit profile button|leads to edit profile page|Yes||
|Delete profile|leads to delete confirmation modal|Yes||
|Page layout|As expected|Yes||


#### Volunteer edit their profile page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Nav links|Top left and lead to home page and stay on edit profile respectively|Yes||
|Page title|Edit profile and warning nothing saved till click submit|Yes||
|Form|Contains expected information|Yes||
|Form|Contents checked against admin version of that profile|Yes||
|Form|Clear which data and labels match|Yes||
|Form|Helper text stands out|Yes||
|Form|Verbose names making it human readable|Yes||
|Form Layout|As expected|Yes||
|Submit button|Saves new profile data and retains unchanged data|Yes||
|Page layout|As expected|Yes||
|JS validation|Alert works when first name empty|Yes||
|JS validation|Alert works when last name empty|Yes||
|JS validation|Alert works for letters or number not being 11 digits for the phone number|Yes||
|JS validation|Alert works if no skill is selected|Yes||
|JS validation|Alert work if hours per week negative|Yes||
|Form content|hours per week won't accept letters etc.|Yes||
|Form content|hours per week accepts 0|Yes||
|JS validation|Alert works if hours per week exceeds hours in a week|Yes||
|Form content|Accepts positive number in hours per week (with above exclusions)|Yes||
|JS validation|Alert work is days per week negative|Yes||
|Form content|days per week won't accept letters etc.|Yes||
|Form content|days per week accepts 0|Yes||
|JS validation|Alert works if days per week exceeds hours in a week|Yes||
|Form content|Accepts positive number in days per week (with above exclusions)|Yes||
|Form content|Will allow every timeslot to be accepted and save|Yes||
|Form content|Will allow random selection of timeslots to be accepted and save|Yes||
|Form content|Will allow no timeslots to be selected and save|Yes||
|Form content|Will allow one timeslot to be selected and save|Yes||
|Form content|Will allow text in the skills description box and save|Yes||
|Form content|Will allow no text in the skills description box and save|Yes||
|Form content|Will allow one skill selection to save|Yes||
|Form content|Will allow all skills selected to save|Yes||
|Form content|Will allow random selection of skills to save|Yes||
|Url|Can enter form using url if logged in|Yes||
|Url|Can't enter form using url if not logged in|No access|404 error page|
|back button|Can enter and use form via back button if logged in|Yes||
|back button|Can't enter form by back button if not logged in|No access|404 error page|
|message|generates update message at top of screen for 2.5 seconds when saved|Yes||

#### Volunteer delete their profile
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Delete button|Delete button takes you to modal|Yes||
|Delete button|Doesn't delete till modal confirmation|Yes||
|Delete modal|Can be closed via close button without deleting|Yes||
|Delete modal|Can be closed by clicking anywhere outside the modal|Yes||
|Delete modal|Delete button on modal closes modal and deletes User,Role and Profile for the volunteer|Yes||
|Delete|There is no data that shouldn't be left in database|Yes||
|Delete|When complete moves you to index|Yes||

#### Coordinator dashboard page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|layout|Looks as expected|Yes||
|title|incorrect place|Yes||
|volunteers awaiting activation|Number correct against database|Yes||
|Coordinators awaiting activation|Number correct against database|Yes||
|Coordinators awaiting activation|First names all displayed correctly|Yes||
|Search for volunteer button|works|Yes||
|Activate volunteers button|Works|Yes||
|Add charity button|Works|Yes||
|Update charity button|Works|Yes||
|Search for coordinator profile button|Works|Yes||
|back button|can be reached by back button when logged in|Yes||
|back button|can't be reached by back button by logging in as volunteer|No access|error 500|
|back button|Can't be reached by back button when not logged in|No access|error 500|
|url|Can be reached by url when logged in as a coordinator|Yes||

#### Coordinator activate/edit coordinator profiles page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|As expected|Yes|Pre search and post search|
|placeholder|gives information on what to search|Yes||
|Search coordinator |Finds all coordinators if nothing entered|Yes||
|Search coordinator |Finds correct coordinator with search|Yes||
|Search coordinator |Can find multiple coordinators and display|Yes||
|Search coordinators|if a search is entered states how many entries found|Yes||
|search|Coordinators displayed as expected when found|Yes||
|update/activate button|works and send you to correct profile|Yes||
|see profile button|works and sends you to correct profile|Yes||
|delete button|works and sends you to the delete modal|Yes||
|back button|can be reached by back button when logged in|Yes||
|back button|can't be reached by back button by logging in as volunteer|No access|error 500|
|back button|Can't be reached by back button when not logged in|No access|error 500|
|url|Can be reached by url when logged in as a coordinator|Yes||


#### Coordinator search for volunteers page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|As anticipated|Yes||
|Activities select|Correct values showing and can only select 1|Yes||
|Activities select|Each item selectable and held in menu|Yes||
|Day select|Correct values showing and can only select 1|Yes||
|Day select|Each item selectable and held in menu|Yes|||
|slot select|Correct values showing and can only select 1|Yes||
|slot select|Each item selectable and held in menu|Yes|||
|Messages|Starts requesting a search which disappears after search|Yes||
|Messages|After search gives a message of what you searched for|Yes||
|No results|The page just tells you what you searched for|Yes||
|Results|The page shows the relevant information on each of the matches|Yes|Profiles divided by a line with the name in bold|
|Results|Only shows fields that weren't part of the search and are relevant to contacting/matching them|Yes||
|back button|can be reached by back button when logged in|Yes||
|url|Can be reached by url when logged in as a coordinator|Yes||

#### Coordinator activate volunteers search page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|Looks as expected|Yes||
|List of volunteers|laid out properly|Yes||
|List of volunteers|Contains all and only unactivated volunteers|Yes||
|See profile and activate button|Takes you to correct read-only profile to activate|Yes||
|List of volunteers|Only names of volunteers visible on this screen|Yes||
|back button|can be reached by back button when logged in|Yes||
|url|Can be reached by url when logged in as a coordinator|Yes||

#### Coordinator can activate volunteer
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|Looks as expected|Yes||
|Data for volunteer|laid out properly|Yes||
|Data for volunteer|read only so coordinators can't change|Yes||
|Data|Only interactive part activate tick box|Yes||
|Tick box|Can be ticked or unticked and submited|Yes||
|Tick box|activated status is changed according to the tick box status|Yes||
|submit|Returns to list of to be activated and if person was activated they are no longer on the list|Yes||
|back button|can be reached by back button when logged in|Yes||

#### Coordinator add charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|Looks as anticipated|Yes||
|in puts|no inputs can be left empty|Yes|Built in warning|
|Coordinators|only one coordinator selected|Yes||
|Coordinators|all coordinators selected|Yes||
|Coorindator|random coordinators selected|Yes||
|Charity name|limited to 50 characters|yes|Stops taking input at 50 characters|
|back button|can be reached by back button when logged in|Yes||
|url|Can be reached by url when logged in as a coordinator|Yes||

#### Coordinator choose charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|looks as anticipated|Yes||
|Message|In place and clear to read|Yes||
|Search box|Placeholder clear|Yes||
|Search box|searched capital letters gives result whether capital or small|Yes||
|Search box|searched small letters gives result whether capital or small|Yes||
|Starting message|You need to enter a charity is on screen till search|Yes||
|After search|You searched for .... details correct|Yes||
|After search|if nothing found to match this search did not find any charities message|Yes||
|After search|all appropriate charities found and displayed appropriately|yes||
|Look at charity button|Takes you to correct charity readonly page|Yes||
|update charitybuttn|Takes you to update charity page|Yes||
|back button|can be reached by back button when logged in|Yes||
|url|Can be reached by url when logged in as a coordinator|Yes||


#### Coordinator edit charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|as expected|Yes||
|Inputs|displayed with labels and helper information promient|Yes||
|Inputs|Contains correct information for that charity|Yes||
|Coordinators|Several or one can be chosen|Yes||
|Coordinators|cannot be left blank|Yes||
|Submit|Saves information|Yes||
|message|message confirming update on top of screen for 2.5 seconds when submited|Yes||
|back button|can be reached by back button when logged in|Yes||

#### Coordinator readonly charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Layout|As expected|Yes||
|Correct data|Matches admin database and is for correct charity|Yes||
|coordinators|displays multiple (or however many there are)coordinators|Yes||
|back button|can be reached by back button when logged in|Yes||

#### Coordinator delete charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Delete button|Delete button takes you to modal|Yes||
|Delete button|Doesn't delete till modal confirmation|Yes||
|Delete modal|Can be closed via close button without deleting|Yes||
|Delete modal|Can be closed by clicking anywhere outside the modal|Yes||
|Delete modal|Delete button on modal closes modal and deletes CharityProfile for selected charity|Yes||
|Delete|There is no data that shouldn't be left in database|Yes||
|Delete|When complete moves you to dashboard|Yes||
|message|generates update message at top of screen for 2.5 seconds when deleted|Yes||

#### Coordinator delete Coordinator Profile

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Delete button|Delete button takes you to modal|Yes||
|Delete button|Doesn't delete till modal confirmation|Yes||
|Delete modal|Can be closed via close button without deleting|Yes||
|Delete modal|Can be closed by clicking anywhere outside the modal|Yes||
|Delete modal|Delete button on modal closes modal and deletes CharityProfile for selected charity|Yes||
|Delete|There is no data that shouldn't be left in database|Yes||
|Delete|When complete moves you to index|Yes||
|message|generates update message at top of screen for 2.5 seconds when deleted|Yes||

Unlike with the volunteer delete which completely removes the user this one is intended to just remove the personal details. This did leave the role and login details intact.


#### Flash messages

Most activities that involve change contain a flash message. Other activities such as searches are apparent by the messages on the screen or results being displayed. These flash / results messages have been checked at each of the relevant activities. They were all found to be working.

#### Superuser/admin activities

The admin site was checked for showing all the data that is in the database. As this was not written as part of this project very limited testing was done of the functionality of the buttons etc.

The most important actions that would need to be done for this site that can't be done via the normal login as either volunteer or coordinator are:

**Skill choices cannot be added/edited/deleted**

- Added, deleted and updated the list of activities through the skill choices model in the admin area as a super user successfully.

**Wrong role chosen when signing up**

- If someone has signed up as a coordinator by accident (instead of the volunteer) then the superuser can also remove their username from roles and coordinator profiles and then they can resubmit their details as a volunteer.This was done as part of the testing.

## Browsers

Using Chrome, Firefox and Safari site was tested on computers and iphone.

## Responsiveness

For checks on responsiveness see below document:

[responive](document/responsive.pdf)

## Bugs found in testing that were not fixed due to time constraints

### More validation of coordinator profile required

The coordinator profile works well if you forget to enter anything in one of the boxes it will bring up and alert. However, at the time of testing just before submission when I tried putting in things other than letters or longer than the maximum number of letters this is allow the random numbers etc or long strings to be saved. An urgent future development would be to fix this for better defensive programming.

It is not a bug that will affect significantly the operation of the software as on the dashboard they will be able to see what mistaken entires were made and correct them promptly by editing the coordinator profile. This will not compromise the security of the software as until another coordinator activates a profile it can't do anything except go to the pending page.

### Horizontal Scroll bar

There was often a horizontal scroll bar across the bottom of the page while I was working. I was unable to determine the exact source of the horizontal scroll bar. As this can be worked around with css and overflow-x: hidden, I decided to use this work around for the deployment of the site with the hope of finding the source of the horizontal scroll bar at a later date to solve the problem rather than hide it. as the error is hidden it isn't a top priority to fix.

### Volunteer Profile model

At some point the function :

```
def __str__(self):
    return self.name
```
in the VolunteerProfile in volunteer/models.py lost it's indentation. During testing this caused a problem that some of the profiles had been generated with the function operating and some hadn't. This meant that the admin panel was unable to display the volunteer profiles. To get this working again I was able to delete all the profiles through the functionality on the site back to the point that it had changed and then sign up some volunteers again. This meant that the admin panel was able to access it again as it had only one type of profile. I have left this as it is, but this does mean that the admin panel has less helpful names for the volunteer profile than had previously been used. name has also been removed as a variable from this model. This code was also removed as it is now redundant. This isn't a significant problem as 

### Buttons on 404 and 500

During testing the buttons on the 404 page 500 page seemed to sometime be the intended size and sometime go the full width of the page. It wasn't obvious why this was as the error was intermittent, therefore I was unable to fix this at this time. This isn't a significant problem as the button always worked, just sometimes looked odd.


## User stories

The epic user stories are described below and covered by the manual testing of the pages unless mentioned in the comments.

The user story level and task level issues [issues](https://github.com/RachWalm/VolunteerVillage/issues?q=is%3Aissue+is%3Aopen) were from these epics and so by covering the epics they have been tested. The bugs were all tested after fix and again as above manual testing.

|Issue|Title|Testing comments|
|------|-----|-----|
|[#66](https://github.com/RachWalm/VolunteerVillage/issues/66)(Epic : new to the site )|As a potential volunteer , I can see the site aims and navigate to how it works page so that I can decide whether to use it. | How it works page wasn't implement - therefore, not tested|
|[#61](https://github.com/RachWalm/VolunteerVillage/issues/61)(epic:Volunteer joins site)|As a volunteer, I can join the site and put in my profile so that I can be ready to volunteer.  |Follows manual testing|
|[#65](https://github.com/RachWalm/VolunteerVillage/issues/65)(Epic: Volunteers can only see/update/delete their own information and only when logged in )|As a volunteer, I can join the site and put in my profile so that I can be ready to volunteer.  |Follows manual testing|
|[#63](https://github.com/RachWalm/VolunteerVillage/issues/63)(Epic: Volunteer reads their profile)|As a Volunteer, I can look at the preferences I have chosen so that I can be confident they are correct.|Follows manual testing|
|[#62](https://github.com/RachWalm/VolunteerVillage/issues/62)(Epic: Volunteer update their profile)|As a volunteer, I can update my profile so that I can make any changes as time goes by.  |Follows manual testing|
|[#64](https://github.com/RachWalm/VolunteerVillage/issues/64)(Epic : user can delete profile )|As a Volunteer, I can delete my profile so that I can stop using the site and stop them having access to my details.  |Follows manual testing|
|[#67](https://github.com/RachWalm/VolunteerVillage/issues/67)(Epic : Coordinators can be registered and log in and out)|As a Coordinator, I can register and log in and out so that I can do my job.  |Follows manual testing|
|[#69](https://github.com/RachWalm/VolunteerVillage/issues/69)(Epic: coordinators can be approved)|As a approver, I can get coordinators onto the system so that I can get them coordinating.  |Follows manual testing|
|[#68](https://github.com/RachWalm/VolunteerVillage/issues/68)(Epic : coordinator can search the profiles to find someone to do the volunteering)|As a coordinator, I can search for a suitable volunteer so that I can match the activity to a volunteer.  |Follows manual testing|
|[#104](https://github.com/RachWalm/VolunteerVillage/issues/104)(Epic: Coordinators can activate the volunteers profile)|As a Coordinator, I can look at new profiles and consider them for old projects and then activate them so that I can check for spam and see what is newly available.  |Follows manual testing|
|[#85](https://github.com/RachWalm/VolunteerVillage/issues/85)(Epic: if user isn't logged in but URL for a logged in page typed send to error page)|As a site user, I can **type the url but not be logged in ** so that I can see a useful information error page rather than url not found etc..  |Follows manual testing|
|[#70](https://github.com/RachWalm/VolunteerVillage/issues/70)(Epic: charities section of website set up)|As a coordinator, I can create update and delete and read info on charities so that I can use this as a source of information.  |Follows manual testing|
|[#71](https://github.com/RachWalm/VolunteerVillage/issues/71)(Epic: ratings and notes area of website created)|As a coordinator, I can make notes and rating the volunteers so that I can keep details and keep track of how many hours of volunteering they have done.  |This was a nice to have that wasn't implemented so wasn't tested.|

Since I have started testing the site I would have put in more user stories to deal with malicious or accidental occurences on the site.

## Real world use

This was also tested by my mother Pat Walmsley who has worked a charity that was very similar to the one that I was attempting to design this for. She was able to use the site with ease.