# Volunteer Village

## Introduction

## UX design

### Wireframes

The [wireframes](document/initial-wireframes.pdf) that were built were for an index page to draw in the volunteer, for a volunteer profile page that can be created and updated by people wishing to volunteer, a page explaining how to use the system and a co-ordinators page. Some of these had both large monitor and small device setups displayed.

### Relationship diagram

The different apps and relationships were discussed and as the idea formed a rough initial relationship diagram was developed.

![relationship diagram](document/relationships.png)

## Features

### Existing Features

### Potential Future Feature Developments 

## Bugs

## Technologies

### languages used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used for the coding of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) was included for styles and layout of the site.
- [python 3.11.5](https://docs.python.org/3/) for functionality.


### tools

- [VSCode](https://code.visualstudio.com/) was used to create and edit the website.
- [Git](https://git-scm.com/) was used for the version control and project board to plan the project.
- [Heroku](https://www.heroku.com/) was used to deploy and host site.
- [pythontutor](https://pythontutor.com/render.html#mode=edit) for working though my code step by step so I could gain understanding when it didn't behave as I anticipated.

### Web Resources

- [Chrome-DevTools](https://developer.chrome.com/docs/devtools/) were extremely useful for trying out different code without affecting my core code and particularly when working on responsiveness.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to check for performance and accessibility.
- [HTML-markdown-validator](https://validator.w3.org/) was used to validate the HTML.
- [CSS-validator](https://jigsaw.w3.org/css-validator/) was used to perform the CSS validation.
[PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding

[AmIResponsive](https://ui.dev/amiresponsive).

[coolors](https://coolors.co/)

[Responsive viewer extension](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb) 

### images

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

### Heroku Deployment

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