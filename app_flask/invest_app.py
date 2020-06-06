#!/usr/bin/env python3
"""
The flow to investor
"""
from flask import (
    Blueprint, render_template,
    session, redirect,
    url_for, request)
from datetime import datetime

invest = Blueprint("invest", __name__)

@invest.route("/new_inversion", methods=['GET', 'POST'])
def new_inversion():
    """Create a new inversionobject"""
    from models.inversion import Inversion
    from models.user import User
    
    im_rt = session.get('message')
    if "username" in session:
        
        username = session.get('username')
        date = datetime.utcnow()
        goodDate = date.strftime('%d-%m-%Y')

        if im_rt is True:
            #Add here the code for add a debt
            return render_template("inversions.html", im_rt=im_rt)

        if request.method == "POST":
            cash = request.form['cash']
            try:
                currentUser = User.query.filter_by(email=username).first()
                newInv = Inversion(budget=cash, owner=currentUser)
                newInv.save()
            except:
                # Pass this error if the inversion object not is created
                return render_template("inversions.html", error_inv=True, date=goodDate)
            # If pass the creation
            return render_template("inversions.html", error_inv=False, date=goodDate)
        # If is get method
        return render_template("inversions.html", date=goodDate)
    
    return redirect(url_for("login"))


@invest.route("/my_carter")
def inversions():
    """ My inversions """
    im_rt = session.get("message")
    return render_template("my_carter.html", im_rt=im_rt)

@invest.route("/profile")
def profile():
    """ displays profile template """
    im_rt = session.get("message")
    return render_template("user.html", im_rt=im_rt)

@invest.route("/logout")
def logout_invest():
    return redirect(url_for("logout"))
