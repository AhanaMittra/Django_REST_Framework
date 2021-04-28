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