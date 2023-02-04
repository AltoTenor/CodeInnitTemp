from flask import Flask, redirect, render_template,url_for,request,redirect,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.datastructures import ImmutableMultiDict
import os
from flask import session
import smtplib


port = int(os.environ.get('PORT', 5000))


app=Flask('__name__' ,template_folder=r'C:\Users\AltoTenor\OneDrive\Documents\Python\CodeInnit\LoginPage\venv', static_folder=r'C:\Users\AltoTenor\OneDrive\Documents\Python\CodeInnit\LoginPage\venv\static')
app.secret_key = 'BAD_SECRET_KEY'
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/favicon.png')

@app.route('/',methods=['POST','GET'])
def index():
    
    if request.method=="POST":
        try:
            a=request.form.getlist('email')[0]
            b=request.form.getlist('password')[0]
            session['email']=a
            session['password']=b
            return render_template('Form.html')

       
    else:
        try:
            return render_template('loginpageFINAL.html')
        except:
            return render_template('loginpageFINAL.html')







#Saad Code
@app.route("/api/send_email", methods=["POST"])
def send_email():
    if request.method == 'POST':
        username =session['email']
        password =  session['password']
        print(username)
        print(password)
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']

        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(username, recipient, message)
        server.close()
        return render_template('success.html')
    else:
        return render_template('loginpageFINAL.html')



















if __name__== "__main__":
    app.debug=True
    app.run()