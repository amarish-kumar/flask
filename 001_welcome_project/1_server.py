#Coded by : Rishikesh Agrawani
#Python 2.7.12
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome to flask..."

@app.route("/hygull")
def my_message():
	return "<h1 style='color:green'>Welcome to Hygull</h1>"

if __name__=="__main__":
	app.run()
