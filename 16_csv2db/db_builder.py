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

def create_table(name: str, fields: dict) -> None:
	'''creates a table with the given name and fields
	fields is a dict mapping a field name to its attributes'''
	fields = tuple(fields.items()) #converts fields to a tuple for easy access

	cmd = f"CREATE TABLE {name}("#starter command for row creation
	for i in range(len(fields)): #iterate through fields by index
		cmd += f"{fields[i][0]} {fields[i][1]}"
		if i != (len(fields) - 1): #if this is not the last element in the list, add a comma
			cmd += ", "
		else: #if not, cap it off
			cmd += ");"
	c.execute(cmd)

create_table("roster", {"name":"TEXT NOT NULL", "age":"INTEGER NOT NULL", "id":"INTEGER PRIMARY KEY"})

with open("students.csv", "r") as file: #opens csv file as variable file
	dr = csv.DictReader(file) # reads the file in, with a list with dictionaries where the first row are the keys and the values are the values of the row corresponding to that entry.
	for entry in dr: #for every entry in the DictReader
		c.execute(f"INSERT INTO roster (name, age, id) VALUES (\"{entry['name']}\", {entry['age']}, {entry['id']})") #insert the values in order of name, age, id into the database.


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
