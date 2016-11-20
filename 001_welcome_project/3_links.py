#Coded by : Rishikesh Agrawani
##Python  : 2.7.12
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
	return "<center><h2><i>Welcome to flask...please visit.../hygull to see Green colored centered message...and imp links for flask</i></h2></center>"

@app.route("/hygull")
def my_message():
	links="<a href='https://www.fullstackpython.com/flask.html' target='_blank'>Full Stack Python</a><br>"
	links+="<a href='https://www.tutorialspoint.com/flask/index.htm' target='_blank'>flask tutorial on tutorialspoint</a><br>"
	return "<center><h1 style='color:green;text-align:center'>Welcome to Hygull</h1>"+links+"</center>"

if __name__=="__main__":
	app.debug=True	
	app.run()		#run(host,port,debug,options)....127.0.0.1, 5000, False,To be forwarded to underlying Werkzeug server
	app.run(debug=True)

'''
Debug mode:
	A Flask application is started by calling the run() method. However, while the application is under development, 
	it should be restarted manually for each change in the code. To avoid this inconvenience, enable debug support. 
	The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors 
	if any, in the application.
'''

#The Debug mode is enabled by setting the debug property of the application object to True before running or passing the #debug parameter to the run() method.

