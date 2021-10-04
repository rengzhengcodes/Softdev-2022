from flask import Flask #imports the flask class
from occupation_generator import random_job, job_percentages #imports the function that generates the random job + the weighted probabilities

app = Flask(__name__) #creates an instance of the Flask class
@app.route("/")
def main():
	job = random_job()
	jobs = str(tuple(job_percentages.keys()))
	template =  """EAR (Edwin Zheng, Angela Zheng, Renggeng Zheng) <br/>
	Random Occupation: {occupation} <br/>
	Possible Occupations: {jobs}"""
	template = template.format(occupation = job, jobs = jobs) #template string that then gets formatted via kwargs
	return template
app.run()
