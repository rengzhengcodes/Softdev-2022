# EAR (Edwin Zheng Angela Zhang Renggeng Zheng)
# SoftDev
# K10 - Flask Learning Day 2, the Flaskening
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
# True means we turned on website debug mode.
# EDIT: it said it did, but what did it do?
# Starting printout changed to:
	#"* Serving Flask app 'app' (lazy loading)
	# * Environment: production
	#   WARNING: This is a development server. Do not use it in a production deployment.
	#   Use a production WSGI server instead.
	# * Debug mode: on
	# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	# * Restarting with stat
	# * Debugger is active!
	# * Debugger PIN: 125-144-047
	#"
app.run()

# Besides that nothing changed. We do not know where to enter the debugger PIN.
# EDIT: further versions showed no new knowledge.
	# Console did not work. EDIT: nothing we found in browser dev tools did either
# Runs the server when you import it from another file
