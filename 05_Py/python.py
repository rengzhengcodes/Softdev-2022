#Renggeng Zheng
#SoftDev
#K05 -- Improved 01_Py with New People
#2021-09-24

##enables debug print statements
DEBUG = False
##if this exists as a txt you can import it, but we do not have a txt, json, csv, etc of names
##names are listed last, first initial b/c that is convention in most systems + sorts by last name then first name
pd1 = open("pd1_names.txt", "r").read().strip().split("\n") #list storing names for pd1 kids imported from file.
pd2 = open("pd2_names.txt", "r").read().strip().split("\n") #list storing names for pd2 kids imported from file.
##sorts names if inputs are not already so they are in alphabetical order like on an attendance roster
pd1.sort()
pd2.sort()

if DEBUG:
	print(pd1, pd2) #checks that sort works in DEBUG mode

pd_chosen = input("What period's name do you want? ") #allows CLI input for which period
pd_chosen = int(pd_chosen) #converts input into an integer
name_index = input("Input the index of the name you wish to retrieve (0-based): ") #allows CLI input to retrieve a specific name
name_index = int(name_index) #converts input into an integer

if pd_chosen == 1:
	print("Name: " + pd1[name_index])
else:
	print("Name: " + pd2[name_index])
