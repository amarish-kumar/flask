
#Created  			: 01 December 2016.
#Python(version)    : 2.7.12
#Coded by 			: Rishikesh Agrawani
#Request            : I have commented the lines...Just read that...It is very important.
#Note				: You will/can or won't/can't get get many errors while scripting this script.
#					  (1) Forgetting to include render_template,
#					  (2) Forgetting to start the app...app.run()...etc.
#					  (3) raise TemplateNotFound(template)..........wrong template name

from flask import request,Flask,render_template

app=Flask(__name__,template_folder="./templates") 	  #templates folder is the default...
													  #So don't need to specify...
													  #If we are not placing our html files inside templates
													  #then it becomes argent to specify the directory path 

@app.route("/setcookie")
def get_cookie():
	cookieValue=request.cookies.get("^MyUserName$")
	if cookieValue==None:						  #Don't use cookieValue=""...If cookie is not set...then it will be None
		#print "Cookie named ^MyUserName$ is not set..."						"""Error line"""
		msg= "Cookie named ^MyUserName$ is not set..."
		return render_template("cookie_is_set_or_not.html",msg=msg)
	else:
		#print "Extracted cookie(^MyUserName$) value is : "+cookieValue			"""Error line"""
		msg="Extracted cookie(^MyUserName$) value is : "
		return render_template("cookie_is_set_or_not.html",msg=msg)	

if __name__=="__main__":
	app.run()	#NameError: name 'app' is not defined........If we don't import Flask and these 
				#2 lines





