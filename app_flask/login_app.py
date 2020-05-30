#!/usr/bin/env python3
"""
Create the log in and the register of users
"""
import user
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Creacion de la API
app = Flask(__name__)
# Coneccion con la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/crowdlending'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Rutes
@app.errorhandler(404)
def not_found(error):
    """If the route not is there"""
    return "Page Not Found", 404

@app.route("/", strict_slashes=False)
def main():
    """Render the main tenplate"""
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Make the login"""
    if request.method == "POST":
        session.pop("user_id", None)

        username = request.form['username']
        password = request.form["pass"]

        print("The user is {} and your password is {}".format(username, password))
        userLog = user.User.query.filter_by(email=username)
        if userLog.pwd == password:
            session["user_id"] = userLog.id
            return redirect(url_for("/i"))

        return "Your email or password is wrong", 200

    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Make the register"""
    return "profile template", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

@app.route("/i", strict_slashes=False)
def Init_page():
    """The template inside of the app"""
    return "You are in", 200
