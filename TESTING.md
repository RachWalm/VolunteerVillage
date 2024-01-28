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

###[add_profile](document/lightcoadd-profile.png)

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

#check each page against role to view it and logged in and activated

### Pages

#### Base on every page

Unless stated tested on index page, but visual check on every page - will be noted if doesn't work on any page tried.

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
|||||
|||||
|||||
|||||
|||||
|||||



#### Log in page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Log out page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Role choice page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Page layout|Looks as expected|Yes||
|Volunteer|sign up as volunteer select|Yes||
|Coordinator|Sign up as coordinator select|Yes||
|Multiple|Can't sign up as both|Yes||
|Submit volunteer|submitting saves as volunteer|Yes||
|Submit coordinator|submitting saves as coordinator|||
|||||
|||||
|||||
|||||



#### Pending activation page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Volunteer add profile page

|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|Page title|Create your profile|Yes||
|Form|Contains expected boxes|Yes||
|Form|Clear which data and labels match|Yes||
|Form|Helper text stands out|Yes||
|Form|Verbose names making it human readable|Yes||
|Form|Layout|As expected|Yes|
|Submit button|Saves new profile data|||
|Page layout|As expected|Yes||
|JS validation|Alert works when first name empty|Yes||
|JS validation|Alert works when last name empty|Yes||
|JS validation|Alert works for letters or number not being 11 digits for the phone number|Yes||
|JS validation|Alert works if no skill is selected|Yes||
|JS validation|Alert work is hours per week negative|Yes||
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
|Form content|Will allow random selection of timeslots to be accepted and save|||
|Form content|Will allow no timeslots to be selected and save|Yes||
|Form content|Will allow one timeslot to be selected and save|||
|Form content|Will allow text in the skills description box and save|Yes||
|Form content|Will allow no text in the skills description box and save|Yes||
|Form content|Will allow one skill selection to save|Yes||
|Form content|Will allow all skills selected to save|Yes||
|Form content|Will allow random selection of skills to save|Yes||
|Url|Can enter form using url if logged in|Yes||
|Url|Can't enter form using url if not logged in|No entry|404 error page|
|back button|Can enter and use form via back button if logged in|Yes||
#|back button|Can't enter form by back button if not logged in||
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
|Table|Layout|As expected||
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
|Form|Layout|As expected|Yes||
|Submit button|Saves new profile data and retains unchanged data|Yes||
|Page layout|As expected|Yes||
|JS validation|Alert works when first name empty|Yes||
|JS validation|Alert works when last name empty|Yes||
|JS validation|Alert works for letters or number not being 11 digits for the phone number|Yes||
|JS validation|Alert works if no skill is selected|Yes||
|JS validation|Alert work is hours per week negative|Yes||
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
|Url|Can't enter form using url if not logged in|No entry|404 error page|
|back button|Can enter and use form via back button if logged in|Yes||
|back button|Can't enter form by back button if not logged in|No entry|404 error page|
|message|generates update message at top of screen for 2.5 seconds when saved|Yes||





#### Volunteer delete their profile
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator dashboard page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator activate/edit coordinator profiles page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator search for volunteers page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator activate volunteers page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator add charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator choose charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator edit charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator delete charity page
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||

#### Coordinator can activate volunteers
|Feature|How tested|Result|Comments|
|---|-----|-----|-----|
|||||


#### Flash messages

Most activities that involve change contain a flash message. If the user performs an allauth related activity (login/logout etc.) or if the user updates the database in some way a flash message should appear on the screen for 2.5 seconds. Other activities such as searches are apparent by the messages on the screen or results being displayed.

#### Superuser/admin activities

Most activities can be performed by the users in one role or another, with the exception of various searches and filters which are on the specific pages. 

- Added, deleted and updated the list of activities through the skill choices model in the admin area as a super user.
- Found and updated a Coordinator profile


Database updates/creations/deletions can also be performed in the admin section of the site.

If someone has signed up as a coordinator that shouldn't have then the superuser can also remove their username from roles and coordinator profiles and then they can resubmit their details as a volunteer.

### Testing data added to database

## Browsers

## Responsiveness

For checks on responsiveness see below document:

[responive](document/responsive.pdf)

## Bugs

## User stories