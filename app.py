# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/1006summary")
def summary():
    return render_template("1006summary.html")

#start the server
if __name__ == "__main__":
    app.run()