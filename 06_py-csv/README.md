# EAR (Edwin Z., Angela Z., Renggeng Z.) Explains CSV and Weighted Probabilities
Softdev <br/>
K06 -- Explanation of reading in from a CSV and weighted probabilities <br/>
2021-09-29 <br/>

## File (CSV) I/O. Mostly the I
File CSV io was handled with the CSV library. We used the DictReader() function to read in a CSV as a dictionary. It was not in the format we liked (it was formatted as ```{"Job Class": job_name, "Percentage": percentage}``` while we wanted ```{job_name: percentage}```), so used a tuple (an ordered, unchangeable list) of the values of the dictionary to rearrange it and remove the data we didn't need.
## Dictionary: What is it good for? How does one use?
A dictionary is good for mapping one non-numeric value to another value. One uses a dictionary much like a list, with a key in [] mapping to a value in the dictionary.
## list:
1. Basics of github-flavoured markdown (Raison d'etre? How does one learn?)
	* Github markdown uses # to mark a header and multiple #'s to make smaller headers.
	* --- makes a line.
	* Use ```<br/>``` for a new line.
	* Use \`\`\`code\`\`\` for code snippet inclusions
	* Use * for bullet points.
	* Use \\ before special characters to type them.
2. Weighted randomization:
	* Need a way to tie it to a random number generator.
	* Need a way to keep track of the options the randomly generated number does not correspond to.
	* Need a list of weights to work with.
## Maximize Clarity
(Probably) done
