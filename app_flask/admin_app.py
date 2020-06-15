#!/usr/bin/env python3
"""
The flow to investor
"""
from flask import (
    Blueprint, render_template,
    session, redirect,
    url_for, request)
from datetime import datetime
from hashlib import md5

admin = Blueprint("admin", __name__)


@admin.route("/new_debts", methods=['GET', 'POST'])
def new_debts():
    """All postulations debts"""
    from models.user import User

    if "admin-session" in session:
        users = User.query.all() 
        user_dict = {}

        for user in users:
            user_dict[user.document] = []
            for debt in user.debts:
                if debt.state == "In progress":
                    user_dict[user.document].append(debt)
        print(user_dict)

        return render_template("admin.html", user_dict=user_dict)

    return redirect(url_for('admin.admin_login'))


@admin.route("/", methods=['GET', 'POST'])
@admin.route("/login", methods=['GET', 'POST'])
def admin_login():
    """Logic for admin"""
    from models.admin import Admin

    if 'admin-session' in session:
        return redirect(url_for('admin.new_debts'))

    elif request.method == "POST":

        username = request.form['username']
        password = request.form["password"]

        md5PwdConfirm = md5(password.encode('utf-8')).hexdigest()
        userLog = Admin.query.filter_by(username=username).first()

        params = [username, password]

        for n in params:
            if len(n) == 0:
                return render_template("login_adm.html", error_fill=True)
        try:
            if userLog.pwd == md5PwdConfirm:
                session['admin-session'] = username
                return redirect(url_for("admin.new_debts"))

            return render_template("login_adm.html", error_pwd=True)
        
        except:
            return render_template("login_adm.html", error_pwd=True)

    return render_template("login_adm.html")


@admin.route("/register", methods=['GET', 'POST'])
def admin_register():
    """
    Easy register of a new admin.
    Beta system
    """
    from models.admin import Admin

    if "admin-session" in session:
        return redirect(url_for("admin.new_debts"))

    if request.method == "POST":
        names = request.form["names"]
        last_names = request.form["lastNames"]
        username = request.form["email"]
        password = request.form["password"]

        params = [names, last_names, username, password]

        for n in params:
            if len(n) == 0:
                return render_template("register_adm.html", error_params=True)

        allAdmins = [admin.username for admin in Admin.query.all()]

        if username in allAdmins:
            return render_template("register_adm.html", error_exist=True)

        else:
            md5Pwd = md5(password.encode('utf-8')).hexdigest()
            try:
                newAdmin = Admin(names, last_names, username, md5Pwd)
            except:
                return render_template("register_adm.html", error_data=True)

            newAdmin.save()
            session['admin-session'] = username
            return redirect(url_for('admin.new_debts'))

    return render_template("register_adm.html")


@admin.route("/logout")
def admin_logout():
    """Admin logout"""
    if "admin-session" in session:
        session.pop('admin-session')

    return redirect(url_for("admin.admin_login"))