"""
SQLite3 database connection using SQL Alchemy Core
"""

import sqlalchemy as db

# connect to the database
engine = db.create_engine('sqlite:///movies1.db')
connection = engine.connect()

# access the metadata of the database
metadata = db.MetaData()
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# Adding record into the table
query = movies.insert().values(Title='Lust Stories', Director='Karan Johar', Year=2018)
connection.execute(query)

# Selecting all the data
query = db.select([movies])
# Filtering by year
#query = db.select([movies]).where(movies.columns.Year == 1995)

# Execute query
result_proxy = connection.execute(query)

# Fetch the query results
result_set = result_proxy.fetchall()

print(result_set)