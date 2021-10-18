#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K15 -- Session Greetings -- Usernames and Passwords
#2021-10-18

from flask import Flask, request, render_template

server = Flask(__name__)
header = """#Team02 - Renggeng Zheng Ivan Lam Lia Nelson"""


@server.route('/', methods=["GET"])
def main():
	'''displays login page'''
	return render_template("login.html", header=header) # renders our login with our header

@server.route('/auth', methods=["POST", "GET"])
def authenticate():
	'''autenticates login info'''
	if request.method != "POST":
		return render_template("login.html", header=header,login_status="Wrong method used to access login. Must use POST")
	if request.form["u_name"] == "admin" and request.form["p_word"] == "admin":
		return render_template("response.html", header=header, username = request.form["u_name"]) # user greeting + our header
	else:
		return render_template("login.html", header=header, login_status="Username or PW is incorrect.") #returns the index page if the login isn't correct + tells the user the input wasn't right

if __name__ == "__main__": #false if this file imported as module
	#enable debugging, auto-restarting of server when this file is modified
	server.debug = True
	server.run()
