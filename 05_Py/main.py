#Renggeng Zheng
#SoftDev
#K05 -- Improved 01_Py with New People
#2021-09-24

# SUMMARY OF TRIO DISCUSSION:
## A large list is not a maintainable solution to the issue of name storage. Error detection is needed for any input solution besides a crash to an error message as users would probably not understand it if they are laymen. Files are also nice as they are more laymen friendly then tinkering with the code. It also prevents introducing some errors in the code as you are limited to messing with the input rather than the entire algorithm.
# DISCOVERIES:
## Print statements are good at debugging.
## Python does not have as rigid compile-time type checks as Java so watch out.
## Python also does not do string typecasting like Java.
# QUESTIONS:
## Would a dict not be more expandable?
## Storing and reading names from a JSON or CSV might be better if library downloads were allowed I believe?
## exec() might be good here for the dynamism the code needs versus the lines of if else statements?
# COMMENTS:
## Good practice in communication and group work.
## Good commenting makes code easier to understand.
## Good formatting also enhances code readability.

##enables debug print statements
DEBUG = True
##if this exists as a txt you can import it, but we do not have a txt, json, csv, etc of names
##names are listed last, first initial b/c that is convention in most systems + sorts by last name then first name
pd = {
	1: open("pd1_names.txt", "r").read().strip().split("\n"), #list storing names for pd1 kids imported from file.
	2: open("pd2_names.txt", "r").read().strip().split("\n"), #list storing names for pd2 kids imported from file.
}
##sorts names if inputs are not already so they are in alphabetical order like on an attendance roster
pd[1].sort()
pd[2].sort()

if DEBUG:
	print(pd[1], pd[2]) #checks that sort works in DEBUG mode

try:
	pd_chosen = input("What period's name do you want? ") #allows CLI input for which period
	pd_chosen = int(pd_chosen) #converts input into an integer
	name_index = input("Input the index of the name you wish to retrieve (0-based): ") #allows CLI input to retrieve a specific name
	name_index = int(name_index) #converts input into an integer

	if pd_chosen in pd.keys(): #checks period exists
		print("Name: " + pd[pd_chosen][name_index])
	else:
		print("This period: " + str(pd_chosen) + " does not exist. Exiting program.")
		exit(1)
	print("Exiting")
	exit(0)
except (IndexError, ValueError):
	from random import randint,randrange #imported here so as not to cause unecessary imports if this path is not triggered
	print("Invalid input detected. Choosing random student: ")
	pd_chosen = tuple(pd.keys())[randrange(len(pd.keys()))]
	if pd_chosen in pd.keys():
		print("Name: " + pd[pd_chosen][randrange(len(pd[pd_chosen]))])
	else: #no one should get here because of the randInt limitations so this shouldbe fine
		print("You should not be here! Error! Error!")
		exit(1)
