"""
SQLite3 database connection using Python Database Specification API

"""

import sqlite3

connection = sqlite3.connect("movies1.db")

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
    (Title TEXT, Director TEXT, Year INT)''')


# famousFilms = [('Coolie No 1', 'David Dhawan', 1995),
# ('Ludo', 'Anurag Basu', 2020),
# ('Udta Punjab', 'Abhishek Chaubey', '2016')]

# Add data into the database
# Adding single record
#cursor.execute("INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)")
# Adding multiple records
#cursor.executemany("INSERT INTO Movies VALUES(?,?,?)", famousFilms)

# Retrieve data from the database
# Selecting all data
#records = cursor.execute("SELECT * FROM Movies")
# Filtering the results
release_year = (1995, )
cursor.execute("SELECT * FROM Movies WHERE Year=?", release_year)


# Print on the console
# for fetching single record
# print(cursor.fetchone())
# for fetching all 
print(cursor.fetchall())

connection.commit()
connection.close()


