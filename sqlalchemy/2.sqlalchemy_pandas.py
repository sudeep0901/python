import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt

engine = db.create_engine('mysql+mysqlconnector://root:admin@localhost:3306  /sakila')
connection = engine.connect()
results = engine.execute('SELECT * FROM actor LIMIT 10')
print(results)

query = 'select * from actor'
actor_df = pd.read_sql_query(query, engine)
print(actor_df.head())

plt.show(actor_df.hist())
# fetch_result = results.fetchone()
# print(type(fetch_result))

# for item in fetch_result.items():
#     # print(type(item))
#     print(item, item[0], item[1])

# other_results = results.fetchall()

# print(type(other_results))

# for litem in other_results:
#     print(litem)


print(engine.table_names())
