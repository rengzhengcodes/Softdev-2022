# EAR (Edwin Z., Angela Z., Renggeng Z.)
Softdev <br/>
K06 -- Explanation of reading in from a CSV and weighted probabilities <br/>
2021-09-29 <br/>

## File (CSV) I/O. Mostly the I
File CSV io was handled with the CSV library. We used the DictReader() function to read in a CSV as a dictionary. It was not in the format we liked, so used a tuple (ordered, unchangeable list) of the values of the dictionary to rearrange it and remove the data we didn't need.
## Dictionary: What is it good for? How does one use?
A dictionary is good for mapping one non-numeric value to another value. One uses a dictionary much like a list, with a key in [] mapping to a value in the dictionary.
## list:
1. Basics of github-flavoured markdown (Raison d'etre? How does one learn?)
	a. Github markdown uses # to mark a header and multiple #'s to make smaller headers.
	b. --- makes a line.
	c. use "<br/>" for a new line.
2. Weighted randomization:
	a. Need a way to tie it to a random number generator.
	b. Need a way to keep track of the options the randomly generated number does not correspond to.
	c. Need a list of weights to work with.
## Maximize Clarity
