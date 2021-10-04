# EAR (Edwin Zheng Angela Zhang Renggeng Zheng)
# SoftDev
# K10 - Flask Learning Day 2, the Flaskening
# 2021-10-04

# Nothing has changed output-wise from V3.
# For V4 it now seems that it only runs app if the python file is the main one called. EDIT: true
# Debugger stuff still not figured out. EDIT: currently still true
# It runs nothing if you just import the file from another file. Edit: true


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
