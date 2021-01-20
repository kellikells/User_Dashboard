# User Dashboard

------------------------------------------------------------

# App's Purpose:
- Registered users setup their own public profile
- Users can leave messages on other user's profile page
- Users can comment on messages 
- Administrators can remove users, messages, and comments

============================================================

## Technologies Utilized:
- Django
- Python
=============================================================

## Developer Techniques:
- Django Model Template View (MTV) structure


=============================================================

## Setup



------------------------
create virtual environment

# Mac:
> virtualenv -p python3 djangoPy3Env
> source djangoPy3Env/bin/activate
(djangoPy3Env)> pip install Django==1.10

# PCs:
> virtualenv djangoPy3Env
> call djangoPy3Env/Scripts/activate
(djangoPy3Env)> pip install Django==1.10
------------------------

> django-admin startproject main
> cd main
# Make a new apps directory
> mkdir apps
# Navigate into apps
> cd apps
------------------------
# Bash: (Mac, Linux)
  > touch __init__.py
# PCs: (Command Prompt)
  > nul> __init__.py
------------------------

> python ../manage.py startapp first_app

------------------------

  # Inside main/settings.py
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  # BECOMES:
   INSTALLED_APPS = [
       'apps.first_app', ### added this line!
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
------------------------


Go to your main folder and run python manage.py runserver from the terminal. Then proceed to localhost:8000. 

=============================================================


 ### Screenshots of the app's functions:


![initial load](/apps/static/dashboard_1.jpg)

--------------------------------------------------------------

--------------------------------------------------------------

--------------------------------------------------------------

--------------------------------------------------------------

--------------------------------------------------------------

--------------------------------------------------------------

