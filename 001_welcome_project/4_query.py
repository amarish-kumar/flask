#Coded by : Rishikesh Agrawani
#Python 2.7.12
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome to flask...visit /hygull/Rishikesh.....Or /hygull/AnyName"

@app.route("/hygull/<string:prog_language>")
def my_message(prog_language):
	return "<center><h1 style='color:green'>Welcome to Hygull</h1><h2>"+prog_language+"</h2></center>"

if __name__=="__main__":
	app.debug=True
	app.run()
	app.run(debug=True)
