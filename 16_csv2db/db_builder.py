#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K16 -- Relational Databases -- SQLite
#2021-10-20
#Time Spent: 7.5 People Hours

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

	cmd = f"CREATE TABLE IF NOT EXISTS {name}("#starter command for row creation
	for i in range(len(fields)): #iterate through fields by index
		cmd += f"{fields[i][0]} {fields[i][1]}"
		if i != (len(fields) - 1): #if this is not the last element in the list, add a comma
			cmd += ", "
		else: #if not, cap it off
			cmd += ");"
	c.execute(cmd)

def fill_table(table: str, filename: str) -> None:
	'''table = table you want to fill
	filename = csv you're importing
	headers = dict matching csv header names to field header names'''

	with open(filename, "r") as file: #opens csv file as variable file
		dr = csv.DictReader(file) # reads the file in, with a list with dictionaries where the first row are the keys and the values are the values of the row corresponding to that entry.
		dr = tuple(dr) #so we can subscript it
		csv_headers = tuple(dr[0].keys())# gets header by checking the keys of the firt element of the DictReader.
		sql_fields = "(" #generates the sql_fields we'll feed to the command
		for i in range(len(csv_headers)):
			sql_fields += csv_headers[i]
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

				if i != (len(csv_headers) - 1): #if its not the last element, add a comma
					values += ", "
				else:
					values += ")"
			if not exists(table, entry):
				c.execute(f"INSERT INTO {table} {sql_fields} VALUES {values}") #insert the values correlating to csv headers database. Sql_fields in case fields are a different order from the csv, so everything goes to the right place
def exists(table: str, record: dict) -> bool: # checks if a record already exists
	where_query = "";
	for field, value in record.items():
		where_query += field #adds field to where_query
		if type(value) is str: #adds quotes to query for strings for equality checks
			where_query += f" = \"{value}\""
		else:
			where_query += f" = {value}"
		where_query += " AND " #connects elements
	where_query = where_query[0:-5] # strips last AND
	# print(where_query)
	c.execute(f"SELECT COUNT(1) FROM {table} WHERE {where_query}")
	# print(c.fetchone()[0])
	return c.fetchone()[0] != 0 #if it does not exist, it returns 0 from fetchone()
#creates roster of students
create_table("roster", {"name":"TEXT NOT NULL", "age":"INTEGER NOT NULL", "id":"INTEGER PRIMARY KEY"})
fill_table("roster", "students.csv")
#creates course table
create_table("courses", {"code":"TEXT NOT NULL", "mark":"INTEGER NOT NULL", "id":"INTEGER NOT NULL"}) #here, ids overlap
fill_table("courses", "courses.csv")
#==========================================================

db.commit() #save changes
db.close()  #close database
