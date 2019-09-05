import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker
import datetime
# import category
metadata = MetaData()


class Category(object):
    def __init__(self, category_id, name, last_update):
        self.category_id = category_id
        self.name = name
        self.last_update = last_update


def _get_date():
    return datetime.datetime.now()

category_table = Table('category', metadata,
                Column('category_id', Integer, primary_key=True),
                Column('name', String(25)),
                Column('last_update', onupdate = datetime.datetime.now)
                )

category_mapper = mapper(Category, category_table)
cat_gt_10 = category_table.select(Category.category_id > 10)

engine = db.create_engine(
    'mysql+mysqlconnector://root:admin@localhost:3306/sakila', echo = True)
connection = engine.connect()
 
session = sessionmaker()
session.configure(bind=engine)
my_session = session()
all_category = my_session.query(Category).all()
print(all_category)
first_category = my_session.query(Category).first()
print(first_category.name, first_category.category_id, first_category.last_update)
first_category = my_session.query(Category.category_id, Category.last_update, Category.name).first()
print(first_category)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FilmText(Base):
    __tablename__ = 'film_text'
    film_id = Column(db.Integer, primary_key =  True)
    title = Column(db.String(255))
    description = Column(db.String(255))
    def __repr__(self):
        return super().__repr__()


first_fiml_text = my_session.query(FilmText).first()
print(type(first_fiml_text))
print(first_fiml_text.description, first_fiml_text.film_id, first_fiml_text.title)
filter_film_text = my_session.query(FilmText).filter_by(title='ACE GOLDFINGER').all()
print(filter_film_text)
for ft in filter_film_text:
    print(ft)