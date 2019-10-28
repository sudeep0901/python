django-admin startproject pollsite
python manage.py runserver

python manage.py startapp polls

python manage.py migrate

python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001
python manage.py migrate
python manage.py shell
coverage run --source=polls  manage.py test
coverage report -m

# PACKAGING DJANGO App for resue in other app

setup tools
1. First, create a parent directory for polls, outside of your Django project. Call this directory django-polls.
2. Move the polls directory into the django-polls directory.
3. Create a file django-polls/README.rst with the following contents:
5. Create a django-polls/LICENSE file. 