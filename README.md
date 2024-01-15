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

#### Index page

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

Most activities can be performed by the users in one role or another.

One activity that is superuser exclusively able to do is the option for the super user to change the list of activities that can be selected and searched for. This action only needs to be performed once and both selection and search will be updated. 

Database updates/creations/deletions can also be performed in the admin section of the site.

If someone has signed up as a coordinator that shouldn't have then the superuser can also remove their username from roles and coordinator profiles and then they can resubmit their details as a volunteer.

### Testing data added to database


### Potential Future Feature Developments 

comments and likes area

area to save activity requests from public and charities that haven't been fullfilled.

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
[PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding

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