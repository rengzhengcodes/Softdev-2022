from flask import Flask #imports the flask class
from occupation_generator import random_job, job_percentages #imports the function that generates the random job + the weighted probabilities

app = Flask(__name__) #creates an instance of the Flask class
def main():
	job = random_job()
	jobs = str(job_percentages.keys())
	return
	"""EAR (Edwin Zheng, Angela Zheng, Renggeng Zheng) \n
	Random Occupation: {occupation} \n
	Possible Occupations: {jobs}""".format(occupation = job, jobs = jobs) #template string that then gets formatted via kwargs

app.run()
