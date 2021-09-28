# imports our main file
import main

results = dict()
results["total"] = 100000
for run in range(results["total"]):
	output = main.random_job()
	if output in results.keys():
		results[output] += 1
	else:
		results[output] = 1

print("Job, Percentage") #format of print statements
sorted_jobs = list(results.keys())
sorted_jobs.sort()
for job in sorted_jobs:
	print(job + " : " +  str(results[job] / results["total"] * 100))

