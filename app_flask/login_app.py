#!/usr/bin/env python3
"""
Create the log in and the register of users
"""
import user
from flask import Flask, render_template, request, session, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5

# Creacion de la API
app = Flask(__name__)
# Coneccion con la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/crowdlending'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'esto-es-una-clave-secreta'

# Rutes
@app.errorhandler(404)
def not_found(error):
    """If the route not is there"""
    return "Page Not Found", 404

@app.before_request
def before_request():
    """Confirm if have a session"""
    g.user = None

    if 'username' in session:
        sessionUser = user.User.query.filter_by(email=session['username']).first()
        g.user = sessionUser

@app.route("/i", strict_slashes=False)
def home():
    """The template inside of the app"""
    if not g.user:
        return redirect(url_for('login'))
    else:
        return "You are in", 200

@app.route("/", methods=["GET", "POST"], strict_slashes=False)
@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Make the login"""
    if 'username' in session:
        return redirect(url_for('home'))

    elif request.method == "POST":

        username = request.form['username']
        password = request.form["password"]

        md5PwdConfirm = md5(password.encode('utf-8')).hexdigest()
        userLog = user.User.query.filter_by(email=username).first()

        try:
            if userLog.pwd == md5PwdConfirm:
                session['username'] = username
                return redirect(url_for("home"))
        except:
            return "Your email or password is wrong", 200

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Make the register"""
    if request.method == "POST":
        names = request.form["names"]
        last_names = request.form["lastNames"]
        email = request.form["email"]
        password = request.form["password"]
        confirmPwd = request.form["confirmPassword"]

        if password != confirmPwd:
            return "The password and the confimation not make match", 200

        allUsers = [user.email for user in user.User.query.all()]

        if email in allUsers:
            return "The email alredy exists", 200
        else:
            md5Pwd = md5(password.encode('utf-8')).hexdigest()
            newUser = user.User(names, last_names, email, md5Pwd)
            newUser.save()
            session["username"] = email
            return redirect(url_for('home'))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
