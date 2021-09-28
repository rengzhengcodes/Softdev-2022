# imports our main file
import main

results = dict()
results["Total"] = 100000
for run in range(results["Total"]):
	output = main.random_job()
	if output in results.keys():
		results[output] += 1
	else:
		results[output] = 1

print("Job, Percentage, Expected") #format of print statements
sorted_jobs = list(results.keys())
sorted_jobs.sort()
for job in sorted_jobs:
	if job == "Total": #want to print this at the end for formatting clarity
		continue
	if job != "Other": #necessary because the job "Other" is not explicitly defined in the original
		print(job + " : " + str(results[job] / results["Total"] * 100) + " : " + str(main.job_percentages[job]))
	else:
		print(job + " : " + str(results[job] / results["Total"] * 100) + " : " + "0.2")

print("Total" + " : " + str(results["Total"] / results["Total"] * 100) + " : " + str(main.job_percentages["Total"]))
