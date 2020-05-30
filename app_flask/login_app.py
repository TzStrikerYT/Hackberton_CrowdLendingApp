#!/usr/bin/env python3
"""
Create the log in and the register of users
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models.user import User, db

# Creacion de la API
app = Flask(__name__)
# Coneccion con la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/crowdlending'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.create_all()

# Rutes
@app.errorhandler(404)
def not_found(error):
    """If the route not is there"""
    return "Page Not Found", 404

@app.route("/", strict_slashes=False)
def main():
    """Render the main tenplate"""
    return "MAIN PAGE", 200

@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Make the login"""
    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]

        userLog = User.query.filter_by(email=username)
        if userLog.pwd == password:
            return "Your password is correct", 200
        else:
            return "Your email or password is wrong", 200

@app.route("register", methods=["GET", "POST"])
def register():
    """Make the register"""
    return "profile template", 200

if __name__ == "main":
    app.run(host="0.0.0.0", port="5000")
