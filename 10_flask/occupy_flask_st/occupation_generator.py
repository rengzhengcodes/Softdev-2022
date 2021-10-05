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
	if DEBUG:
		random.seed(a=42) #sets seed for predictable testing

	#upper bound is 100 as despite the exclusive end, we are including 0 in our set of rng numbers
	#Step is 0.1 because that's the accuracy to which the data is to.
	number_rolled = random.randrange(0, 1000, 1) / 10 #randrange does not accept floats as inputs, so we make do
	debug_print(number_rolled)
	#sum of probabilities of jobs iterated through. Uses DND esque DC check, with a job's given DC/valid range
	#being the end of the previous job's upper bound and its own upper bound.
	current_dc = 0
	debug_print(probability_book)
	for job, probability in probability_book.items(): #grabs the job and its associated probability
		current_dc += probability #adds the currrent probability to the probability DC
		# strictly less than because the first number has the segment from 0 to its number.
		# if we did <= the rest of the segments would be off by 0.1 as the first has the inclusive 0 as well.
		if number_rolled < current_dc and job != "Total":
			return job #DC is reached, which means the number generated corresponds to thsi job, so return it.
	return "Other" #our thing does not neatly add up to 100%, as 0.2% of people work in other industries. This is the failthrough case.
