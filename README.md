# Volunteer Village

## Introduction

The volunteer village site was designed to be used by people in two roles. 

The first role is as a volunteer looking to provide voluntary assistance. The second is as a coordinator at Volunteer Village who's attempting to match people who are in need of assistance with appropriate assistance. The volunteer signs up and provides contact information and details of what kind of assistance they are able to provide and when they are free on a weekly basis in a profile form which is saved. 

The second role of coordinator can search the volunteers profiles to be given a list of people who can provide that type of assistance at that time. The coordinator also works with specific charities so has a section to record information on their charities for their own memory and if it needs to be cross-referenced/used by other coordinators. In this way coordinators can match charities (or individuals who contact the organisation) with volunteers and external to the site help them connect.

## UX design

The aim is to have a landing page that is enthusiastic about volunteering. This should hook the volunteer without making it seem like hard work. From there a new user (coordinator or volunteer) can sign up, select their role and fill out a profile form.

As a volunteer they can then see their profile, edit it and delete their personal details from the account, with the current functionality.

As a coordinator you can activate accounts, modify and delete other coordinators / your own account. It is anticipated that this would be a small voluntary organisation so no HR/IT department to modify other coordinators - but joining or leaving or name changes would need to be operational by coordinators of each other.

Next a coordinator will need to be able to search the list of volunteers by activity and when they are likely to be available, then read their contact details to contact them. So there is a search for volunteers, but this doesn't have any modification/creation/deletion function as their personal data is to stay under control of the volunteers.

Coordinators will also activate the volunteer profiles. This is a manual check which has two purposes, to check it isn't a spam profile and to consider if there is already known opportunities for them to volunteer.

Coordinators will also have their own charities that they work with, there is a section for them to record information in a text box about their charities. There is a link showing which coordinators and charities work together.

On every page there is the logo for volunteer village which is based around a helping hand coming out of the dark surrounded by holding hands circle motif and has the words volunteer village in the centre. This is mirrored in the favicon on the tab.

### Wireframes

The initial [wireframes](document/initial-wireframes.pdf) that were built were for an index page to draw in the volunteer, for a volunteer profile page that can be created and updated by people wishing to volunteer, a page explaining how to use the system and a coordinators page. Some of these had both large monitor and small device setups displayed. Wireframes were not created for the nice to have pages at this stage such as the charities section and feedback and likes section. 

### Relationship diagram

The different apps and relationships were discussed and as the idea formed a rough initial relationship diagram was developed.

![relationship diagram](document/relationships.png)

## Features

### Existing Features

Every page that should only be used by coordinators checked that that only authenticated people can us it in the HTML with an if user.is_authenticated and a check by the function in views role_authenticate, which checks if they are of the correct role and if they have been activated by a coordinator.

#### Index page

The index page has the same basic heading and footer that is on every page. 

The heading contains a logo, title and the home page and allauth navigation links. It also contains a message as to whether you are logged in (and who you are logged in as) or if you are not logged in. This area also has flash messages when they are relevant.

The footer has information about the developer and project is for Code Institute.

#### Sign up page

This page is built by allauth, but also has the header and footer as previously described.

#### Log in page

#remember me and forgotten password

This page is built by allauth, but also has the header and footer as previously described.

#### Log out page

This page is built by allauth, but also has the header and footer as previously described.

#### Role choice page

This page is part of the sign up process. As users can either be signing up as a volunteer or as a part of the organisation as a coordinator. The dropdown select has volunteer as the default and only visible when you get to the page as this should be the main option chosen. It can then be changed to coordinator by coordinators.

This page currently only has the option of volunteer or coordinator, this could be simply updated as each role is associated with a number to allow for additional roles, such as charity login or different types of coordinator should the organisation grow to require that coordinators are more focused or want the activations restricted to certain personnel. 

Currently, 1 is volunteer and 2 is coordinator. Where it is required that access is blocked 0 has been returned as in the function role_authenticate which is used to restrict pages bringing up their content unless it is a coordinator who is activated.

#### Coordinator add profile page

As the information on this page will be visible to all the coordinators it doesn't contain excessive personal information, it just requests first and last name. This should be sufficient for information connection to the coordinators.

#### Pending activation page

As the coordinators will have access to almost all functions and large quantities of data, there is then a step where another coordinator needs to activate the coordinator. This will prevent accidental or malicious access as a coordinator. This is the page that the coordinator is directed to between them signing up and being activated - even if they log out and back in. If they inform another coordinator that they need activating other coordinators can perform this.

#### Volunteer add profile page

If the role of volunteer has been picked then this takes you to the add profile page. There is little action that a volunteer would want to take without a profile. This page requests information such as name, phone number to contact to volunteer with volunteering opportunities. It also establishes which of the activities from the list they would like to do and when they are regularly available. There is a free text box to add any special skills etc that they want to have highlighted. The information on form for the phone number is Javascript validated to ensure that it is a phone number. The number of hours and days is restricted to the number of hours and days in a week through Javascript validation.

#### Volunteer read their profile page

The volunteer is sent to their profile read page when they have added their profile, or log in with a profile in place. Here they can see the information that is held on them. There is also the option to edit the profile - which sends them to a page to perform that(described below), or delete their profile (which is described below).

This isn't editable on this page to avoid accidental clicking and making corrections.

#### Volunteer edit their profile page

If a volunteer clicks to edit their profile then they are directed to a page that is similar to the form to add their original profile but is populated with the currently held information. To edit they must make the relevant changes to the form and then press submit. Unless submit is pressed no changes will be performed.

#### Volunteer can delete the profile information

If a volunteer no longer wants their information to be held then they can choose to delete the information. In the read volunteer profile page there is a delete button, this leads only to their details so they can't delete others details. The delete button doesn't instantly delete it goes to a Javascript coded modal which informs them that the delete cannot be undone and then has the delete button or a cancel button. This prevents unintentional deletion by an accidental button click.

It does allow the user to remove their information but retain their sign in. Once they have confirmed the delete it takes them back to be able to fill out a blank profile as there is little that they can use the site for without a profile.

#### Coordinator dashboard page

This is where active coordinators get sent when they log in and is the centre for all the links that they will need to perform the daily requirements.

# needs fleshing out

#### Coordinator activate/edit coordinator profiles page

If a coordinator signs up to the site there needs to be a restriction on their access as they will have functionality and data access that shouldn't be freely available, so another coordinator has to activate them by ticking the box and submitting. This page can also be used if the coordinator wishes to change their name - marriage, legally changed name etc. As it isn't anticipated that an organisation like this would have an HR sort of role name changes will have to be done by the coordinators. Also should a coordinator leave temporarily such as materinity leave, then the account will need to be deactivated to restrict access to the information on this page. 

As there is a many to many relationship from charities the coordinator also is removed from displaying against that charity.

Although the functionality to delete coordinators is currently in place, this may need to be deactivated were the commenting on the volunteers activities to be implemented. As if that were implemented and coordinators were making the comments and being recorded as making the comments then deleting the coordinator could be problematic. This functionality is here currently as it has no impact on other functionality and might be useful. Were it necessary to remove this functionality to allow other things that require legacy data to function properly then then activate function could be used to deactivate coordinator restricting their access but not their history.

In the event there are no coordinators activated this could be performed for one coordinator by the superuser in the admin section. 

#### Coordinator search for volunteers page

When a request has been made to the organisation for a type of activity to be performed during a certain part of the week a coordinator can go to the search page and select the activity and the day and whether it is for morning/afternoon/evening and if any of the volunteers fit this description then their name is displayed as a list. The information about the volunteers is then displayed in a non-editable table on screen. Coordinators could then contact the volunteers and organise the activity that is required. 

#### Coordinator activate volunteers page

Coordinators are required the activate the volunteers for two reasons. To look at incoming volunteers and see if there are any unfullfilled volunteering opportunities that would suit them. Getting people as they join the site will increase enthusiasm for the process, also to ensure that the database doesn't get filled up with spam profiles. Reading the information provided in the text box by volunteers may also be more useful that just having their choice of activity if they have a special skill that can be matched.

#### Coordinator add charity page

Should a new charity wish to be involved then the coordinator can click on the link in the dashboard and add the charity name and a few details in the text box about the charity's needs and information. The charity can also be assigned a coordinator (or two with a back up, or many for a big charity). Then the information is there as to who to get to deal with a charity's request, or if they are away hopefully enough information is in the text box for someone else to assist.

#### Coordinator choose charity page

Once a charity is in the database then coordinators will want access to the information to read/edit/delete. This page allows coordinators to search by the name (partial or full) of the charity and returns a list of the charities that fit the searched text. For each charity there is a look at charity information (which is non-editable to avoid accidental update), an edit and delete button if they need to change the information or if the charity decides to no longer continue the connection.

#### Coordinator view charity page

When the Look at charity information button is pressed a read only version of the information is presented.

#### Coordinator edit charity page

On the choose charity page there is the option to edit the charity. This takes you to a form that is the same format as the add charity form, except it is populated with the currently held information, which can be altered. No changes will take effect until the submit button is pressed.

#### Coordinator delete charity 

In the choose charity page there is a delete button, this leads only to the details of the selected charity so they can't delete others details. The delete button doesn't instantly delete it goes to a Javascript coded modal which informs them that the delete cannot be undone and then has the delete button or a cancel button. This prevents unintentional deletion by an accidental button click.

Deleting a charity does not delete any of the coordinators that are stated in the many to many relationship as this is not a ON_CASCADE relationship.

#### Navigation bars
The top right navigation bar is for login/signup/logout functionality related to allauth and not specific to the type of user logged in. Or to go to the home page.

#### Logged in/out at top of page

In the top right of the screen next to the nav bar there is an information message that either tells you that you are "Not logged in"  or who you are logged in as (people may have a coordinator and volunteer account).

#### Flash messages

Most activities that involve change contain a flash message. If the user performs an allauth related activity (login/logout etc.) or if the user updates the database in some way a flash message should appear on the screen for 2.5 seconds. Other activities such as searches are apparent by the messages on the screen or results being displayed.

#### Superuser/admin activities

Most activities can be performed by the users in one role or another.

One activity that is superuser exclusively able to do is the option for the super user to change the list of activities that can be selected and searched for. This action only needs to be performed once and both selection and search will be updated. 

Database updates/creations/deletions for everything can also be performed in the admin section of the site.

If someone has signed up as a coordinator by mistake that shouldn't have or maliciously then the superuser can also remove their username from roles and coordinator profiles and then they can resubmit their details as a volunteer - or not if they didn't want to be a volunteer.

If there are no coordinators activated (so no one can activate other coordinators) a coordinator can also be activated in the admin panel in the coordinators profile, then the usual procedure for activating coordinators can proceed.

### Testing data added to database


### Potential Future Feature Developments 

comments and likes area

area to save activity requests from public and charities that haven't been fullfilled. And historic information

Improve the model for the days and times as it would be much better if I had managed to use the initial idea of monday = 1 Tuesday = 2 etc and am = 1 pm =2 so then monday am would be 11, this would have given a simpler and lesser number of fields. However, with problems (described in bugs) doing the initial volunteer create profile and time constraints it was decided to go simple for booleans. This would also have made searching for the volunteers that fitted the criteria required simpler. If I had infinite access to more knowledgeable developers I would have discussed this approach with them as I believe it would have saved time in other areas such as the coordinators search of the volunteers.

Once information has been gathered from the text box entries of the coordinators and volunteers entries there, an assessment of the data to look for recurring themes that could be made into fields rather than them typing it out would be a good step.

real time or calendar inputs for emergency or one of events

coordinator can change volunteers availability when weekly stuff occurs to already volunteering. and record volunteering being done.

follow up tools for coordinators

volunteers can search the charities with the permission of the charity.

section to request assistance.

relate amount of time available to commited already time.

## Bugs

## Technologies

### Languages used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used for the coding of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) was included for styles and layout of the site.
- [python 3.11.5](https://docs.python.org/3/) for functionality.
### Frameworks and libaries
- Django
- Boostrap


### Tools

- [VSCode](https://code.visualstudio.com/) was used to create and edit the website.
- [Git](https://git-scm.com/) was used for the version control and project board to plan the project.
- [Heroku](https://www.heroku.com/) was used to deploy and host site.
- [pythontutor](https://pythontutor.com/render.html#mode=edit) for working though my code step by step so I could gain understanding when it didn't behave as I anticipated.

### Web resources

- [Chrome-DevTools](https://developer.chrome.com/docs/devtools/) were extremely useful for trying out different code without affecting my core code and particularly when working on responsiveness.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to check for performance and accessibility.
- [HTML-markdown-validator](https://validator.w3.org/) was used to validate the HTML.
- [CSS-validator](https://jigsaw.w3.org/css-validator/) was used to perform the CSS validation.
- [PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding

[AmIResponsive](https://ui.dev/amiresponsive).

[coolors](https://coolors.co/)

[Responsive viewer extension](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb) 

### Images

<a href="https://www.freepik.com/free-photo/man-cutting-grass-with-lawn-mover-back-yard_8828103.htm#query=mowing%20lawn&position=0&from_view=search&track=ais&uuid=1f1d6d2e-ade9-4baf-b4d2-4fda06f92667#position=0&query=mowing%20lawn">Image by senivpetro</a> on Freepik

### Libraries

allauth

go through requirements.txt

https://pypi.org/project/django-select-multiple-field/

this needed django utils six installed

https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices
https://django-phonenumber-field.readthedocs.io/en/latest/

https://stackoverflow.com/questions/20138049/redirect-user-to-another-url-with-django-allauth-log-in-signal

Django documentation

## Deployment

### Heroku deployment

The deployed version can be accessed on Heroku [here](https://black-jack21-fa4b7e8cb0bf.herokuapp.com/)

1. [Heroku](https://www.heroku.com/) was used to deploy.
2. Once logged onto the website, using the drop down menu in the top right we went to the dashboard.
![dashboard](document/go-to-dashboard.png)
3. From here we are able to create a new app either by clicking on the icon (which is what we did)

![icon](document/create-new-app.png)

or the drop down menu

![dropdown](document/create-new-app-dropdown.png)

4. Next the app was named black-jack21 and the Europe region chosen in these fields

![name](document/name-and-region.png)

and the purple 'create' button was pressed.

5. In the menu navigation bar the 'settings' was selected

![settings](document/settings.png)

6. The section with Config Vars was then opened up by clicking the Reveal Config Vars button

![reveal](document/reveal.png)

7. The URL's were set, disable_collectstatic was set to 1, port was set to 8000 and the secret key was provided the value.

![configvars](document/config.png)

8. Now we used the menu navigation bar again, this time to select deploy

![nav](document/nav-bar.png)

9. The deployment method was selected by clicking on the GitHub icon and it stated that it was connected to github

![method](document/choose-git.png)

10. The repository was chosen by searching my github

![find](document/find.png)
![connect](document/connect.png)
![connected](document/connected.png)

11. Automatic deployment was chosen so that it would update every time the changes were pushed to git

![auto](document/auto.png)

12. It was deployed

![deployed](document/deployed.png)

### Local Deployment

You will need to pip install the following apps:

Django and gunicorn

```pip3 install django gunicorn```

dj database url and psycopg2

```pip3 install dj_database_url psycopg2```

cloudinary

```pip3 install dj3-cloudinary-storage```

Phone number field

```pip install "django-phonenumber-field[phonenumberslite]"```


pip install django-bootstrap5

pip install whitenoise

pip install django-allauth

<!-- select multiple from a list - not used as required loads of other apps installed see below and some weren't compatible : used multiple choice field from forms instead

```pip install django-select-multiple-field```

select multiple from a list requried additionally django utils six installed

```pip install django-utils-six```
```pip install django-utils``` -->

### Cloning

1. In the git hub repository, code button clicked
2. clicked local
3. choose HTTPS
4. link copied
5. went to terminal (version control) and input the following :git clone https://github.com/RachWalm/VolunteerVillage.git

The project was cloned.


### Forking

## Testing 

See [Testing](TESTING.MD)

## Credits


## Acknowledgements

My Mentor - Juliia Konn has been extremely enthusiastic and provided encouragement and a great deal of support.

My family - Pat Walmsley and Sarah Walmsley have tested the site on their own devices and given very useful feedback.

My Partner - Ian Harris who has been extremely supportive while I have been working on this project.

Code institute - For all the information and course content that has contributed to the creation of this project. 



Women receiving shopping
Image by <a href="https://www.freepik.com/free-photo/people-bringing-supplies-neighbors_19535236.htm#query=companionship%20volunteering&position=17&from_view=search&track=ais&uuid=2f1dea90-1275-4815-984c-bcc37292cb49">Freepik</a>

Drinking tea
No attribution required	
https://pxhere.com/en/photo/180168

driving

Image by <a href="https://www.freepik.com/free-photo/people-helping-old-neighbor_19535511.htm#query=driving%20volunteering&position=1&from_view=search&track=ais&uuid=addf44f7-640b-4aa8-9100-d3ec883618e9">Freepik</a>

Man fixing sink
<a href="https://www.freepik.com/free-photo/man-fixing-kitchen-sink_2893988.htm#page=2&query=DIY&position=26&from_view=search&track=sph&uuid=2ee109c1-c1dc-42e7-b7d4-3f96cf994dce">Image by rawpixel.com</a> on Freepik

Messy desk
https://pxhere.com/en/photo/1294988?utm_content=shareClip&utm_medium=referral&utm_source=pxhere

fundraising
<a href="https://www.freepik.com/free-vector/hand-drawn-minimalist-fundraising-goals-thermometer-vertical-timeline_44590282.htm#query=fundraising&position=23&from_view=search&track=sph&uuid=7136730d-014b-41a6-ad43-7f7a41eb1b75">Image by Wepik</a> on Freepik

Helping at a stall
Image by <a href="https://www.freepik.com/free-photo/people-meeting-community-center_20146042.htm#page=2&query=fundraising&position=1&from_view=search&track=sph&uuid=b3a76a17-f264-4772-8f79-331eaa395a38">Freepik</a>

Litter picking

Image by <a href="https://pixabay.com/users/antranias-50356/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=250044">Manfred Antranias Zimmer</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=250044">Pixabay</a>

Laughing litter pickers

<a href="https://www.freepik.com/free-photo/man-woman-picking-up-trash-from-park-they-collecting-litter-garbage-bag_6889450.htm#page=3&query=environmental&position=18&from_view=search&track=sph&uuid=e79066ba-0560-4981-89b0-f0660cac7f7d">Image by teksomolika</a> on Freepik

Man covered in litter

<a href="https://www.freepik.com/free-photo/photo-surprised-red-haired-man-has-thick-beard-overloaded-with-much-garbage-collects-plastic_11486288.htm#page=4&query=environmental&position=25&from_view=search&track=sph&uuid=f2a5049c-196e-4901-8b94-7425e235573b">Image by wayhomestudio</a> on Freepik

Tutor
<a href="https://www.freepik.com/free-photo/education-concept-student-studying-brainstorming-campus-concept-close-up-students-discussing-their-subject-books-textbooks-selective-focus_1239167.htm#query=tutoring&position=2&from_view=search&track=sph&uuid=5051e72e-6ca4-4128-a144-0e9e94891ca5">Image by mindandi</a> on Freepik

Adult tutoring
Image by <a href="https://www.freepik.com/free-photo/back-view-teacher-student-home_7871378.htm#query=tutoring&position=9&from_view=search&track=sph&uuid=5051e72e-6ca4-4128-a144-0e9e94891ca5">Freepik</a>

Smiling child tutoring
Image by <a href="https://www.freepik.com/free-photo/close-up-father-helping-kid-with-homework_20081813.htm#query=tutoring&position=26&from_view=search&track=sph&uuid=5051e72e-6ca4-4128-a144-0e9e94891ca5">Freepik</a>

Women reading
Image by <a href="https://pixabay.com/users/nigelcohen-2990028/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7321085">Nigel Cohen</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7321085">Pixabay

event
Image by <a href="https://www.freepik.com/free-photo/group-people-volunteering-foodbank-poor-people_15574024.htm#from_view=detail_serie">Freepik</a>

https://compressnow.com/

canava design the logo

search bar

https://www.youtube.com/watch?v=AGtae4L5BbI

https://favicon.io/favicon-converter/

modal for delete from extra blog post on slack