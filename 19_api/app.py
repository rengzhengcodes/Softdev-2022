#Renggeng Zheng
#SoftDev
#K19 -- Using Rest APIs - NASA
#2021-11-23

from flask import Flask, render_template
import json
import urllib

app = Flask(__name__)

@app.route("/")
def index():
	url = "https://api.nasa.gov/planetary/apod?api_key="
	url += str(open("key_nasa.txt", "r").read()) # adds api key onto base url
	## print(url)
	request = urllib.request.urlopen(url) # requests from API with requisite information for a request
	## print(request)
	data = json.loads(request.read()) # reads the returned info from the url and loads the json
	## print(data)
	return render_template("main.html", pic=data['url'], explanation=data['explanation'])

if __name__ == "__main__":  # true if this file NOT imported
	app.debug = True        # enable auto-reload upon code change
	app.run()
