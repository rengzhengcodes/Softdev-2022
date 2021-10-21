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

create_table("roster", {"uname":"TEXT NOT NULL", "uage":"INTEGER NOT NULL", "uid":"INTEGER PRIMARY KEY"})

def fill_table(table: str, filename: str, headers: dict = None) -> None:
	'''table = table you want to fill
	filename = csv you're importing
	headers = dict matching csv header names to field header names'''

	with open(filename, "r") as file: #opens csv file as variable file
		dr = csv.DictReader(file) # reads the file in, with a list with dictionaries where the first row are the keys and the values are the values of the row corresponding to that entry.
		dr = tuple(dr) #so we can subscript it
		csv_headers = None;
		sql_fields = None

		if headers == None:
			csv_headers = tuple(dr[0].keys())# gets header by checking the keys of the firt element of the DictReader.
			sql_fields = "(" #generates the sql_fields we'll feed to the command
			for i in range(len(csv_headers)):
				sql_fields += csv_headers[i]
				if i != (len(csv_headers) - 1): # if its not the last element, add a comma
					sql_fields += ", "
				else:
					sql_fields += ")"
		else:
			csv_headers = tuple(dr[0].keys())# gets header by checking the keys of the firt element of the DictReader.
			sql_fields = "(" #generates the sql_fields we'll feed to the command
			for i in range(len(csv_headers)):
				sql_fields += headers[csv_headers[i]]
				if i != (len(csv_headers) - 1): # if its not the last element, add a comma
					sql_fields += ", "
				else:
					sql_fields += ")"

		for entry in dr: #for every entry in the DictReader
			values = "("
			for i in range(len(csv_headers)):
				header = csv_headers[i] #gets the header at index
				if type(entry[header]) is str: # if the entry is a string add quotes so its not confused with a field
					values += f"\"{entry[header]}\""
				else:
					values += entry[header]

				if i != (len(csv_headers) - 1): #if its not the last element, ad a comma
					values += ", "
				else:
					values += ")"

			c.execute(f"INSERT INTO roster {sql_fields} VALUES {values}") #insert the values in order of name, age, id into the database.

fill_table("roster", "students.csv", {"name":"uname","age":"uage","id":"uid"})
#==========================================================

db.commit() #save changes
db.close()  #close database
