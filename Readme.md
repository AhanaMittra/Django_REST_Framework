Description of packages:
    django -- high level python web-framework for developing secure and maintainable websites.
    djangorestframework -- toolkit for building web APIs.
    black -- python code formatter.
    pylint -- source code, bug, quality checker for python.
    pylint-django -- code quality improvement toolkit for django projects.



Sequence of steps:
1. Make a virtual environment in a folder. 
    python -m venv ~/.virtualenvs/drf          // drf = django rest framework
2. Activate the virtual environment 
    source ~/.virtualenvs/drf/bin/activate [in unix / linux]
    '~/.virtualenvs/drf/Scripts/activate' [in windows]
    Note: If virtualenv is not installed, please install virtual env first. 
            pip install virtualenv
3. Install the required libraries
    pip install django djangorestframework black pylint pylint-django

4. Start a django project
    django-admin startproject RestAPI .
    Note: Here '.' creates the projetfiles directly into the current folder without creating any extra directory.

5. To run the django server.
    ```python 
    python manage.py runserver
    ```

6. Create a library book application.
    python manage.py startapp library

7. As we are using django rest framework and created a library application, we have to include it in the projects       settings.py folder in INSTALLED_APPS list.
```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'library.apps.LibraryConfig',
]
```
8. Go to the models.py inside library folder. Create your own models for using in the database.

9. Enter the command `python manage.py makemigrations`. makemigrations -- Creates individual migration files based on the changes made in the models.

10. Enter the command `python manage.py migrate`. migrate -- Informs the database about the changes made in the models.py .

11. Create a superuser using the command `python manage.py createsuperuser`. Superuser poses administration capabilities. No one else can modify or make changes in databse.

12. Run the django server by `python manage.py runserver`. Then go to the admin page `{Enter_localhost_url}/admin`-> log into your account by the set username and password.

13. In the admin page, we can see there is no new database models that we created. To include the created models in the admin page to add or remove database objects of that model open the admin.py. Add the line `from .models import {Enter_your_model_name}`.

    Register the model by the line `admin.site.register({Enter_your_model_name})`

14. Let us add another field to our created database model. As we have made changes to the database model we have to use makemigrations and migrate command. The commands are entered into the terminal sequentially:
    ```bash
    python manage.py makemigrations library
    python manage.py sqlmigrate library  {migration_name}
    python manage.py migrate
    ```
    The sqlmigrate command shows the sql statements for the corresponding model.

15. Now that we have created our model, let us create a file called `serializers.py`. We use serializers to convert our database models(in this example, Book) to usable representations such as JSON, XML for using in our API.

Note: If there is a problem regarding the import of rest_framework, this may be due to the activation of virtual environment in VScode. To activate the proper environment in VScode, enter `ctrl+shift+p`, search `python:select interpreter`. Enter the path to your virtual environment. 


16. Let's open views.py to create views that will help us to add, remove, update our database using a user interface.
To be reviewed later.

17. Now create a urls.py in the library folder. Which will contain the contents of view and later on it will be conneced with the urls.py of th projects folder which contains all the urls of the applications.

18. To add authentication, enter `from rest_framework import permissions` in the views.py. Add permission_classes to give permissions of access to the user by `permission_classes = [permissions.IsAuthenticationOrReadOnly]`

19. Till now we have implemented BASIC_Auth. To improve our authentication system more than this add `rest_framework.authtoken` to the settings.py file.

20. Now add the authentication schemes to the settings.py file by
    ```python
        REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ]
    }
    ```
    As auth token brings it's own modules with it while installation we have to migrate our project. `python manage.py migrate`.

21. Refresh the page, there will be a field called Auth Token, go to that tokens and generate your own token copy that. Now in Postman go to Authorization there select type of token API Key and there fill the key and value part by 
`key: Authorization  Value: Token {your_token}`.

22. Now install auto documentation like swagger type docs by using the command `pip install drf_spectacular`.
Then add it in the INSTALLED_APPS in settings.py file by `drf_spectacular`.
Then add default schema class in the rest_framework authentication scheme. by `'DEFAULT_SCHEMA_CLASS': "drf_spectacular.openapi.AutoSchema",`