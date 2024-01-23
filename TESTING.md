# Testing

## Validators

### HTML validation

### CSS validation

### Linter Validation

## Lighthouse and accessibility

## Features testing - Manual

check each page against role to view it and logged in and activated

#### Index page

No css colour?

#### Sign up page

#### Log in page

#### Log out page

#### Role choice page

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


Database updates/creations/deletions can also be performed in the admin section of the site.

If someone has signed up as a coordinator that shouldn't have then the superuser can also remove their username from roles and coordinator profiles and then they can resubmit their details as a volunteer.

### Testing data added to database


## Features testing - Automated

## Browsers

## Responsiveness

## Bugs

## User stories