from flask import Flask
from flask import jsonify 

app = Flask(__name__)

@app.route("/details/")
def details():
	"""A function that responses json"""
	details = {"name":"Rishikesh Agrawani","age":24,"link":"pretty/","brother":{'name':'Hemkesh Agrawani',"age":22}}
	print "Returning JSON details..."
	return jsonify(details)

@app.route("/pretty/")
def pretty_details():
	"""A function that requests json and decode it"""
	import urllib2
	import json
	print "JSON..."
	try:
		print "READING..."
		response = urllib2.urlopen("http://localhost:8000/details/")
		print "Got RESPONSE"
		my_details = response.read() #string
		print my_details
		d = json.loads(my_details)
		print "JSON loaded"
		s = "<center>"
		for k,v in d.iteritems():
			if type(v)==type({}):
				l = []
				for key,val in v.iteritems():
					l.append((str(key),str(val)))
				s+=str("<span style='color:gray;font-family:tahoma;font-size:20px;'>"+k+"</span> &nbsp; <span color:green;font-family:helvetica;font-size:20px;>"+str(l)+"</span><hr>")
				continue
			s+="<span style='color:gray;font-family:tahoma;font-size:20px;'>"+k+"</span> &nbsp; <span color:green;font-family:helvetica;font-size:20px;>"+str(v)+"</span><hr>"
		s+="</center>"
		return s
	except:
		print "Error occured..."
		return "<center>An error occured while serving request</center>"

if __name__ == "__main__":
	# app.run()
	app.run(host="0.0.0.0", port=8000, threaded=True) #It is required for different-different requests, like here /details/ & /pretty/ are 2 different sub-urls.
