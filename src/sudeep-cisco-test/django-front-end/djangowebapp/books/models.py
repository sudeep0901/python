from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.TextField('name')
    price = models.IntegerField("price")
    isbn = models.TextField("isbn")
 # id = models.Column(Integer, primary_key=True)
    # name = db.Column(db.String(80), nullable=False)
    # price = db.Column(db.Float, nullable=False)
    # isbn = db.Column(db.Integer)