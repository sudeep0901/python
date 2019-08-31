import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper
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
    'mysql+mysqlconnector://root:admin@localhost:3306/sakila')
connection = engine.connect()
results = engine.execute('SELECT * FROM actor LIMIT 10')
print(results)

query = 'select * from actor'
actor_df = pd.read_sql_query(query, engine)
print(actor_df.head())

plt.show(actor_df.hist())
print(engine.table_names())
category_result = engine.execute(cat_gt_10).fetchall()
print(category_result)