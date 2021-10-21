#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K16 -- Relational Databases -- SQLite
#2021-10-20

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


c.execute("CREATE TABLE roster(name TEXT NOT NULL, id INTEGER PRIMARY KEY, age INTEGER NOT NULL)")
'''everyone has a name, but names can be the same so they cannot be primary keys.
everyone has an age, but those can also be the same so they cannot be primary keys.
everyone has an id, those are unique so they should be primary keys.'''


with open("students.csv", "r") as file: #opens csv file as variable file
	dr = csv.DictReader(file) # reads the file in, with a list with dictionaries where the first row are the keys and the values are the values of the row corresponding to that entry.



command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
