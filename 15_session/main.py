#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K15 -- Session Greetings -- Usernames and Passwords
#2021-10-18

from flask import Flask, request, render_template

server = Flask(__name__)

@server.route('/')
def main():
	'''displays login page'''
	return open("templates/login.html").read()

@server.route('/auth')
def authenticate():
	'''autenticates login info'''
	if request.form["u_name"] == "admin" and request.form["p_word"] == "admin":
		

if __name__ == "__main__": #false if this file imported as module
	#enable debugging, auto-restarting of server when this file is modified
	server.debug = True
	server.run()
