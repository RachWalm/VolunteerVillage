# Testing

## Validators

### HTML validation

The HTML validation is below in a pdf.

[html validation]()

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

[index](document/lightindex.png) - performance could be improved with pictures resized and reformatted - this could be a future improvement.

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

check each page against role to view it and logged in and activated

#### Index page

No css colour?

#### Sign up page

- Filled out sign up page without an e-mail address.
- Filled out with a fake e-mail address

#### Log in page

#### Log out page

#### Role choice page

- Chose the role of Volunteer
- Chose the role of Coordinator

#### Pending activation page

#### Volunteer add profile page

#### Volunteer read their profile page

#### Volunteer edit their profile page

#### Coordinator dashboard page

#### Coordinator activate/edit coordinator profiles page

#### Coordinator search for volunteers page

#### Coordinator activate volunteers page

#### Coordinator add charity page

#### Coordinator choose charity page

#### Coordinator edit charity page

#### Coordinator delete charity page

#### Coordinator can activate volunteers

#### Navigation bars
The top right navigation bar is for login/signup/logout functionality related to allauth and not specific to the type of user logged in.

#### Logged in/out at top of page

In the top right of the screen next to the nav bar there is an information message that either tells you that you are "Not logged in"  or who you are logged in as (people may have a coordinator and volunteer account).

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

## Bugs

## User stories