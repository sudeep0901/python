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