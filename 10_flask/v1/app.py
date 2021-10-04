# EAR (Edwin Zheng Angela Zhang Renggeng Zheng)
# SoftDev
# K10 - Flask Learning Day 2, the Flaskening
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
# seems to tell the code that when a user accesses the website's root (website.com/, it runs the function)
# EDIT: Confirmed
def hello_world():
	# Printouts seem the same despite removal of print(__name__) for all tested methods.
	# EDIT: It's false we just didn't see it.
	return "No hablo queso!"

app.run()
