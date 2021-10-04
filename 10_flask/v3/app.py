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
app.run()
