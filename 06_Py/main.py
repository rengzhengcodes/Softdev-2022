#Renggeng Zheng (EAR - Edwin Z., Angela Z, Renggeng Z.)
#SoftDev
#K06 -- Reading from a CSV
#2021-09-28

#Debug variable
DEBUG = True
#DEBUG PRINTER
def debug_print(var):
	global DEBUG
	if DEBUG:
		print(str(var))

import csv #imports built in csv library
occupations = csv.DictReader(open("occupations.csv", "r")) #imports csv as a dict via rows
job_percentages = dict() #stores jobs mapping to their percentages of workforce
for row in occupations:
	row_values = tuple(row.values()) #gets rid of the unecessary keys information
	job_percentages[row_values[0]] = float(row_values[1]) #maps jobs to their percentages of workforce in dict
debug_print(job_percentages)

