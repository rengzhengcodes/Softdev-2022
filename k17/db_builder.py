#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K17 -- The full stack -- making a wiki
#2021-10-25
#Time Spent: 40 People Minutes

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

class Db_builder:
	def __init__(self, db_file:str = "storage.db"): #initiates a db_builder object by specifying database and initiating self commands
		self.DB_FILE = db_file
		self.db = sqlite3.connect(self.DB_FILE) #open if file exists, otherwise create
		self.c = self.db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

	def create_table(self, name: str, fields: dict) -> None:
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
		self.c.execute(cmd)

	def fill_table(self, table: str, filename: str) -> None:
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
				number_of_values = "("
				list_of_values = list()
				for i in range(len(csv_headers)):
					header = csv_headers[i] #gets the header at index
					list_of_values.append(entry[header])
					number_of_values += "?, " #sql safe replacement

				number_of_values = number_of_values[0:-2] + ")" #removes ending ", " and adds ")"

				if not self.exists(table, entry):
					self.c.execute(f"INSERT INTO {table} {sql_fields} VALUES {number_of_values}", list_of_values) #insert the values correlating to csv headers database. Sql_fields in case fields are a different order from the csv, so everything goes to the right place

	def exists(self, table: str, record: dict) -> bool: # checks if a record already exists
		where_query = "";
		#print(record)
		for field, value in record.items():
			where_query += field #adds field to where_query
			where_query += f"=:{field}" #adds key name for dict-based execute for input safety
			where_query += " AND " #connects elements
		where_query = where_query[0:-5] # strips last AND
		# print(where_query)
		#print(where_query)
		self.c.execute(f"SELECT COUNT(1) FROM {table} WHERE {where_query}", record)
		# print(c.fetchone()[0])
		return self.c.fetchone()[0] != 0 #if it does not exist, it returns 0 from fetchone()

	def exit_db(self): #closes db when object no longer in use
		self.db.commit() #save changes
		self.db.close()  #close database

	def __del__(self): #action upon being deleted
		self.exit_db()

if __name__ == "__main__": #runs if not imported; for testing
	#creates roster of students
	dbb = Db_builder("discobandit.db")
	dbb.create_table("roster", {"name":"TEXT NOT NULL", "age":"INTEGER NOT NULL", "id":"INTEGER PRIMARY KEY"})
	dbb.fill_table("roster", "students.csv")
	#creates course table
	dbb.create_table("courses", {"code":"TEXT NOT NULL", "mark":"INTEGER NOT NULL", "id":"INTEGER NOT NULL"}) #here, ids overlap
	dbb.fill_table("courses", "courses.csv")
	del dbb
