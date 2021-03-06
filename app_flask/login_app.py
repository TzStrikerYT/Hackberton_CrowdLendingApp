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
from app_flask.mail import sendMail
import random

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

@app.route("/landing")
def landing():
    """Show the landing page"""
    return render_template("index.html")


@app.route("/dashboard", methods=['GET', 'POST'], strict_slashes=False,)
def home():
    """The template inside of the app"""
    from models.debt import Debt

    if not g.user:
        return redirect(url_for('login'))
    else:
        im_rt = session.get('message')
        username = session.get('username')
        userObject = user.User.query.filter_by(email=username).first()

        debts = []

        for debt in userObject.debts:
            if debt.state != "Payed":
                debts.append(debt)
       
        if im_rt is None:
            return render_template("dashboard.html", im_rt=im_rt, inversions=userObject.inversions)

        if request.method == "POST":
            state = request.form['state']
            stateAndDebt = state.split(" ")

            debt = Debt.query.filter_by(user_id=stateAndDebt[1]).first()
            if debt.state == "Accepted" or debt.state == "Rejected":
                return render_template("dashboard.html", im_rt=im_rt, debts=debts, no_change=True)    
            elif debt.state == "Postulated":
                debt.confirmation(stateAndDebt[0])
                debt.save()
                return render_template("dashboard.html", im_rt=im_rt, debts=debts)

        return render_template("dashboard.html", im_rt=im_rt, debts=debts, no_change=True)

        return render_template("dashboard.html", im_rt=im_rt, debts=debts)


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
                if userLog.validated == False:
                    session['emailcheck'] = username
                    return redirect(url_for("emailCheck"))

                session['username'] = username
                return redirect(url_for('home'))

            return render_template("login.html", error_pwd=True)
        
        except:
            error = True
            return render_template("login.html", error_pwd=error)

    return render_template("login.html")


@app.route("/logout", strict_slashes=False)
def logout():
    if "username" in session:
        session.pop('username')
        if "message" in session:
            session.pop("message")
    return redirect(url_for('login'))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Make the register"""
    from models import user

    if request.method == "POST":
        names = request.form["names"]
        last_names = request.form["lastNames"]
        email = request.form["email"]
        document = request.form['user_dni']
        phone = request.form['phone']
        password = request.form["password"]
        confirmPwd = request.form["confirmPassword"]

        params = [names, last_names, email, document, phone, password, confirmPwd]
        nums = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for n in params:

            if len(n) == 0:
                error = True
                return render_template("register.html", error_params=error)

        for verify in [document, phone]:
            for lttr in verify:
                if lttr not in nums:
                    return render_template("register.html", error_chr=True) 
        
        if password != confirmPwd:
            error = True
            return render_template("register.html", error_match=error)

        allUsers = [user.email for user in user.User.query.all()]

        if email in allUsers:
            error = True
            return render_template("register.html", error_exist=error)
        else:
            tipo = 'REG'
            keyGen = '{}'.format(random.randrange(10**6))
            data = { 'name': names, 'last_name': last_names, 'code': keyGen }
            sendMail(tipo, email, data)
            md5Pwd = md5(password.encode('utf-8')).hexdigest()
            #try:
            newUser = user.User(names, last_names, email, document, phone, md5Pwd, keyGen)
            #except:
             #   return render_template("register.html", error_data=True)
            newUser.save()
            session["name"] = names
            session["last_names"] = last_names
            session["emailcheck"] = email
            return redirect(url_for('emailCheck'))
    return render_template("register.html")


@app.route("/emailcheck", methods=['GET', 'POST'], strict_slashes=False)
def emailCheck():
    """ Check the correct code sended to email """
    if 'emailcheck' in session:
        info = user.User.query.filter_by(email=session['emailcheck']).first()
        if (request.method == 'POST'):
            if ('regCode' in request.form):
                if request.form['regCode'] == info.reg_cod:
                    info.validated = True
                    info.save()
                    session['username'] = session['emailcheck']
                    session.pop('emailcheck')
                    session.pop('name')
                    session.pop('last_names')
                    return redirect(url_for('home'))
                else:
                    return render_template('checkemail.html', error=True, email=session['emailcheck'])
            elif ('Resend' in request.form):
                tipo = 'REG'
                keyGen = '{}'.format(random.randrange(10**6))
                data = { 'name': session['name'], 'last_name': session['last_names'], 'code': keyGen}
                sendMail(tipo, session['emailcheck'], data)
                info.reg_cod = keyGen
                info.save()
                return render_template('checkemail.html', r_msj=True, email=session['emailcheck'])
    
        return render_template('checkemail.html', email=session['emailcheck'])
    
    return redirect(url_for("register"))


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
                                    rt_response.get('email'),
                                    rt_response.get('identification'),
                                    rt_response.get('telephone'), "")
                newUser.save()

            session['username'] = rt_response.get('email')
            session['message'] = True
            return redirect(url_for('home')) # This redirection need be changed
        else:
            error = True
            return render_template("login_rt.html", error_rt=error)

    return render_template("login_rt.html") #This template needs be changed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
