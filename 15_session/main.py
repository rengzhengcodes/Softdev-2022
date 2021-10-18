#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K15 -- Session Greetings -- Usernames and Passwords
#2021-10-18

from flask import Flask, request, render_template

server = Flask(__name__)
header = """#Team02 - Renggeng Zheng Ivan Lam Lia Nelson"""


@server.route('/', methods=["POST", "GET"])
def main():
	'''displays login page'''
	return render_template("login.html", header=header)

@server.route('/auth')
def authenticate():
	'''autenticates login info'''
	print(request.form)
	if request.form.get("u_name") == "admin" and request.form.get("p_word") == "admin":
		return render_template("response.html", header=header)
	else:
		return render_template("login.html", header=header, login_status="Username or PW is incorrect.")

if __name__ == "__main__": #false if this file imported as module
	#enable debugging, auto-restarting of server when this file is modified
	server.debug = True
	server.run()
