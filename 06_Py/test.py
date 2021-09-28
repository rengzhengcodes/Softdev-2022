import main

results = dict()
results["total"] = 100000
for run in range(results["total"]):
	print(main.random_job())
