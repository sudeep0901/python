<!-- create virtual envrionemnt -->

py -m venv django-env
django-env\Scripts\activate.bat
django-admin startproject  tictactoe
<!-- To start server -->
py manage.py runserver

views.py
url.py

django App
django models writes to databse
<!-- migrations -->
py manage.py showmigrations
py manage.py migrate # cteate table in db usign migration

<!-- crerate django app -->

py manage.py startapp gameplay (name of app)
add new app to settings.py
use model.py to define data structure
# to creaate tables in sql databases
py manage.py sqlmigrate gameplay 0001

py manage.py  makemigrations # update model in gameplay models
py manage.py migrate

django admin site
    register new models game, move to admin.py and start site
    create a user first
        py manage.py createsuperuser

To customize admin option

https://docs.djangoproject.com/en/1.11/ref/contrib/admin/

# get the interactive shell for django application
python manage.py shell
# can import classes in interactive shell
# query all objects from databasein interactive shell
Game.objects.all()
g = Game.objects.get(pk=1) 
Game.objects.filter(status='F')
Game.objects.exclude(status='F')
Game.objects.filter(second_player__username='manasvi') # foriegn table

# QuerySet / Laziness
# each model class has manager object -  Game.Objects that operates on database table


# Model Templates
# static contents
# Shared layout (M Model T Template V View)


