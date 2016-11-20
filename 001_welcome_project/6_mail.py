#Coded by : Rishikesh Agrawani
#Python 2.7.12
from flask import  Flask
from flask_mail import  Mail,Message

app=Flask(__name__)

mail=Mail(app)

mailSender="rishikesh0014051992@gmail.com"
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]="465"
app.config["MAIL_USERNAME"]=mailSender
app.config["MAIL_PASSWORD"]="29915041"
app.config["MAIL_USE_TLS"]=False
app.config["MAIL_USE_SSL"]=True

mail=Mail(app)

@app.route("/")
def home():
	return "<center><h1 style='color:green'>Hello...Send a mail to your emailId...Try to hit 	/mail/YourMail@gmail.com/EmailMessage</h1></center>"

@app.route("/mail/<string:recipient_email>/<string:message>")
def send_mail(recipient_email,message):
	my_message=Message(message,sender=mailSender,recipients=[recipient_email])
	my_message.body="Body Message..."
	mail.send(my_message)
	return "<center><h2 style='color:navy'>Mail successfully Sent to ... "+recipient_email+"</h2></center>"

if __name__=="__main__":
	app.run(debug=True)
