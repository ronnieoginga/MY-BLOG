import flask_mail
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = 'sylveromondi@gmail.com'

    email = flask_mail.Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)