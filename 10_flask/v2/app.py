# EAR (Edwin Zheng Angela Zhang Renggeng Zheng)
# SoftDev
# K10 - Flask Learning Day 2, the Flaskening
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
	# difference was the print statements of print(__name__) and a print statement saying that we're about to print that was added.
	# EDIT: printed the messages in terminal as was previously hypothesized but was missed later because of poor readinhg.
		# when the root page was accessed, the console printed
		#"
		#about to print __name__...
		#__main__
		#127.0.0.1 - - [04/Oct/2021 08:20:19] "GET / HTTP/1.1" 200 -
		#"
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()
