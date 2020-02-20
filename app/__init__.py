from flask import Flask
from flask_mail import Mail
import os
SECRET_KEY= os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = 'enter your mailtrap smtp username'
app.config['MAIL_PASSWORD'] = 'enter your mailtrap smtp password' 

mail = Mail(app)
from app import views
