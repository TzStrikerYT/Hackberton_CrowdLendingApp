#!/usr/bin/env python3
"""
Create the log in and the register of users
"""
from models import user
from app_flask import app
from flask import (
    render_template,
    request, session,
    redirect, url_for, g)
from hashlib import md5
import requests

# Rutes
@app.errorhandler(404)
def not_found(error):
    """If the route not is there"""
    return render_template('404.html'), 404


@app.before_request
def before_request():
    """Confirm if have a session"""
    g.user = None

    if 'username' in session:
        sessionUser = user.User.query.filter_by(
            email=session['username']).first()
        g.user = sessionUser


@app.route("/profile", strict_slashes=False)
def home():
    """The template inside of the app"""
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template("home_invest.html")


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

        params = [username, password]
        for n in params:
            if len(n) is 0:
                error = True
                return render_template("login.html", error_fill=error)

        try:
            if userLog.pwd == md5PwdConfirm:
                session['username'] = username
                return redirect(url_for("home"))
            error = True
            return render_template("login.html", error_pwd=error)
        except:
            error = True
            return render_template("login.html", error_pwd=error)

    return render_template("login.html")


@app.route("/logout", strict_slashes=False)
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

        params = [names, last_names, email, password, confirmPwd]

        for n in params:

            if len(n) == 0:
                error = True
                return render_template("register.html", error_params=error)

        if password != confirmPwd:
            error = True
            return render_template("register.html", error_match=error)

        allUsers = [user.email for user in user.User.query.all()]

        if email in allUsers:
            error = True
            return render_template("register.html", error_exist=error)
        else:
            md5Pwd = md5(password.encode('utf-8')).hexdigest()
            newUser = user.User(names, last_names, email, md5Pwd)
            newUser.save()
            session["username"] = email
            return redirect(url_for('home'))

    return render_template("register.html")

# Make a login and register like a rappitender
@app.route("/login_rt", methods=['GET', 'POST'], strict_slashes=False)
def rappi_login():
    """Make a login and register since rappi api"""

    if 'username' in session:
        return redirect(url_for('home'))

    elif request.method == "POST":

        username = request.form['username']
        password = request.form["password"]

        params = [username, password]
        for n in params:
            if len(n) is 0:
                error = True
                return render_template("login_rt.html", error_fill=error)

        url_courier = 'http://microservices.dev.rappi.com/api/rt-auth-helper/user/type?email={}'.format(username)

        cou = requests.get(url_courier)

        try:
            is_rt = cou.json()
        except:
            print("Not valid JSON")

        print(is_rt.get('user_type'))
        if is_rt.get('user_type') == "courier":

            url = 'http://microservices.dev.rappi.com/api/login/storekeeper'
            headers = {
                'uuid':'550e8400-e29b-41d4-a716-4466554400001234567',
                'platform':'2',
                'Content-Type': 'application/json'
            }
            rappitender = {
                "client_id":"74HzD01JbhZ44iE1kh7Gt6dfNjEKrtWiz0FqTUDQ",
                "client_secret":"W8dOKF1mdHaG9wBNyoOCEBgHajO66GEl81lTDu2P",
                "username":username,
                "password":password,
                "scope":"all"
            }

            r = requests.post(url, headers=headers, json=rappitender)

            try:
                response = r.json()
            except:
                print("Not a valid json, pls verificate the request")
                return "The response cant be convert to JSON", 400

            if response.get('error') is not None:
                error = True
                return render_template("login_rt.html", error_pwd=error)

            url_profile = 'http://microservices.dev.rappi.com/api/storekeepers-ms/storekeeper/rappitendero/profile?cache=false'
            auth = response.get('token_type') + " " + response.get('access_token')
            header_profile = {
                'Content-Type': 'application/json',
                'Authorization': auth
            }
            rt = requests.get(url_profile, headers=header_profile)
            try:
                rt_response = rt.json()
            except:
                print("Not a valid json in the rt request with the token")
                return "Not a valid json in the rt request with the token", 400

            userLog = user.User.query.filter_by(email=rt_response.get('email')).first()

            if userLog is None:
                newUser = user.User(rt_response.get('first_name'),
                                    rt_response.get('last_name'),
                                    rt_response.get('email'), "")
                newUser.save()

            session['username'] = rt_response.get('email')
            return redirect(url_for('home')) # This redirection need be changed
        else:
            error = True
            return render_template("login_rt.html", error_rt=error)

    return render_template("login_rt.html") #This template needs be changed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
