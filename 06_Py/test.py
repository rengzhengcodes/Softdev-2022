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

print(results)
