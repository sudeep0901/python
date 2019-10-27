django-admin startproject pollsite
python manage.py runserver

python manage.py startapp polls

python manage.py migrate

python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001
python manage.py migrate
 python manage.py shell