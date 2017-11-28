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
    emailnos= "@"
    if len(password) > 3 and len(verifypassword) > 3:
        if len(password) < 20 and len(verifypassword) < 20:
            if password == verifypassword:
                if emailnos in email:
                    if " " in password:
                        redirect("/validate")
                    else:
                        return render_template("homepage.html", username=username)
                else:
                    redirect("/validate")
                
    return render_template("signup_form.html", username=username, password=password, verify=verifypassword, email=email)
    
    
app.run()