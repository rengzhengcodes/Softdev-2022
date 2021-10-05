#Renggeng Zheng (EAR - Edwin Z., Angela Z, Renggeng Z.)
#SoftDev
#K06 -- Reading from a CSV
#2021-09-28

# Findings
#1 Knowing a library well and its functionality is better with documentation
## than stabbing blindly in the dark.
#2 Doing frequent run checks is good so that you make sure that you aren't
## working with code that you will have to scrap later because it just doesn't
## work.
#3 Commit frequently in case you need to go back.

## CSV Specific Findings:
#1 The CSV dictreader likes to read it in with the first row as a header for
## the columns of every subsequent node. Very annoying if you don't want that.
#2 Basically an excel spreadsheet with each "cell" being which newline its
## on and how many commas in it is.

# Testing
#1 Testing is very important to verify code integrity. While it might work
## nominally on the surface, there may be hidden, unconsidered complications.
#2 You can import a *.py file in the same directory with a simple import
## statement. This imports both the functions and any defined variables.
#4 All the code in a *.py file (except if it is inside of a function
## declaration is run at the time the file is imported.
##1 Function declarations are also run, but the contents the function is
### wrapping do not.
##2 Basically like the exec() command.

#Debug variable
DEBUG = False
#DEBUG PRINTER
def debug_print(var):
	global DEBUG
	if DEBUG:
		print(str(var))

import csv #imports built in csv library
import random #imports the random library
occupations = csv.DictReader(open("occupations.csv", "r")) #imports csv as a dict via rows
job_percentages = dict() #stores jobs mapping to their percentages of workforce
#formatting it to a more iterable format
for row in occupations:
	row_values = tuple(row.values()) #gets rid of the unecessary keys information
	job_percentages[row_values[0]] = float(row_values[1]) #maps jobs to their percentages of workforce in dict

# debug_print(job_percentages)

#generates a random job given a probability dict formatted {job: percentage with total at the bottom}
def random_job(probability_book = job_percentages): #default argument provided. Valid for an assignment use case.
	# removes total from dictionary
	try: #deletes total line if it exists
		del probability_book["Total"]
	except KeyError:
		pass
	jobs = list(probability_book.keys())
	percentages = list(probability_book.values())

	return random.choices(population=jobs, k=1, weights=percentages)[0]
