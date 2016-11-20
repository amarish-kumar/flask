#Coded by : Rishikesh Agrawani
#Python 2.7.12
from flask import Flask, render_template

app=Flask(__name__,template_folder="./templates/html")

@app.route("/")
def welcome():
	return "Welcome to flask...visit /hygull/Rishikesh.....Or /hygull/AnyName...Or hygull/render"

@app.route("/hygull/<string:prog_language>")
def my_message(prog_language):
	return "<center><h1 style='color:green'>Welcome to Hygull</h1><h2>"+prog_language+"</h2></center>"


@app.route("/hygull/render")
def render_me():
	return render_template("home.html")

if __name__=="__main__":
	# app.debug=True
	app.run()
	# app.run(debug=True)
