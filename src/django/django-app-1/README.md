django-admin startproject djapp01
django-admin help --command
set DJANGO_SETTINGS_MODULE=djapp01.settings
python manage.py runserver 9090
python manage.py startapp customers

python .\manage.py makemigrations blogusers
python .\manage.py sqlmigrate blogusers 0001

python  .\manage.py migrate

python  .\manage.py shell
from blogusers.models import BlogType, BlogUser

from django.utils import timezone

In [4]: bt = BlogType(blog_type="PYTHON",)
BlogType.objects.all()

BlogType.objects.filer(id=1)
BlogType.objects.get(pk=1)

superuser = sudeep
password = sudeep

$ python manage.py startapp polls
