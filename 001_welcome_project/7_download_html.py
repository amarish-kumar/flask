from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_html():
	""" A function that downloads the html content of any webpage and saves it as a given file name"""
	url = raw_input("Enter the URL of any web document whose html you want : ")
	try:
		import urllib2
		response = urllib2.urlopen(url)
		print "Getting html contents from >> ",url
		html = response.read()
		print "Content successfully downloaded."

		print "Please specify the name of target filename : ",
		filename = raw_input()
		with open("docs/download/"+filename,"w") as f:
			f.write(html)
		return "<h2 style='color:green;text-align:center'>Successfully downloaded the html content and saved into a file at ../docs/downlaod/"+filename+"</h2>"
	except:
		print "An error occured, Either you have specified wrong URL or there may be other type of mistake."
		return "<h2 style='color:red;text-align:center'>Check filepath and urls whether they are correct or not.</h2>"

if __name__ == "__main__":
	app.run()
