#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K15 -- Session Greetings -- Usernames and Passwords
#2021-10-18

from flask import Flask, render_template, request, session

server = Flask(__name__)
header = """#Team02 - Renggeng Zheng Ivan Lam Lia Nelson"""


@server.route('/', methods=["GET"])
def main() -> template:
	'''displays login page'''
	return render_template("login.html", header=header) # renders our login with our header

@server.route('/auth', methods=["POST", "GET"])
def authenticate() -> template:
	'''autenticates login info'''
	try:
		if request.method != "POST": #makes sure data is not sent in the url
			return render_template("login.html", header=header,login_status="Wrong method used to access login. Must use POST")
		if request.form["u_name"] == "admin" and request.form["p_word"] == "admin": #pretty sure we should hash the password but this is a proof of concept for the login.
			set_login_cookie()
			return render_template("response.html", header=header, username = request.form["u_name"]) # user greeting + our header
		else:
			return render_template("login.html", header=header, login_status="Username or PW is incorrect.") #returns the index page if the login isn't correct + tells the user the input wasn't right
	except: #catches uncaught errors
		return render_template("login.html", header=header, login_status="Unknown error occured")

def set_login_cookie(): #pass in a template to get cookies
	if request.method == "POST": #check in case we call this elsewhere
		session["u_name"] = request.form["u_name"] #login cookie set

def get_login_cookie() -> str:
	name = request.cookies.get('u_name')
	return name

if __name__ == "__main__": #false if this file imported as module
	#enable debugging, auto-restarting of server when this file is modified
	server.debug = True
	server.run()
