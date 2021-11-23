#Renggeng Zheng
#SoftDev
#K19 -- Using Rest APIs - NASA
#2021-11-23

from flask import Flask, render_template
import requests
app = Flask(__name__) 

@app.route("/")       
def index():
	return render_template("main.html", pic = pic)

if __name__ == "__main__":  # true if this file NOT imported
	app.debug = True        # enable auto-reload upon code change
	app.run()
