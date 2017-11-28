from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    
    return render_template("base.html")



@app.route("/validate", methods=["POST"])
def validate():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verify']
    email = request.form['email']

    if len(password) > 2 and len(verifypassword) > 2:
        if password == verifypassword:
             return render_template("homepage.html", username=username)

    return render_template("signup_form.html", username=username, password=password, verify=verifypassword, email=email)
    
    
app.run()