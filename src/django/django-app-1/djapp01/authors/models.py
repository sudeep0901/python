import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

COUNTRIES = (
    ('IN', "INDIA"),
    ('USA', "United States of America"),
    ('CN', "China"),
    ('RU', "Russia"),
)


class BlogType(models.Model):
    blog_type = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_type


class User(models.Model):
    type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=500)
    country = models.CharField(max_length=100, choices=COUNTRIES)
    create_date = models.DateTimeField('bloger_Creation_Date')
    created_datetime = models.DateTimeField(auto_now_add=True)
    credit_limit = models.IntegerField(default=100000)
    created_by = models.CharField(max_length=100)

    def created_recently(self):
        return self.bloger_create_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.last_name + ", " + self.first_name
