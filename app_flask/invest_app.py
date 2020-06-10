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
    """Create a new inversion object"""
    from models.inversion import Inversion
    from models.user import User

    # Make code for both type users
    im_rt = session.get('message')
    if "username" in session:
        username = session.get('username')
        date = datetime.utcnow()
        goodDate = date.strftime('%d-%m-%Y')

        if im_rt is True:
            #Add here the code for generate debt with the API
            if request.method == "POST":
                the_debt = request.form['cash']
                reason = request.form['motive']

                #put here the API
                #curl --location --request POST 'http://microservices.dev.rappi.com/api/manual-dispersion/debt' \
                #--header 'Content-Type: application/json' \
                #--data-raw '{"debts":[
                #    {
                #    "storekeeper_id":33082,
                #    "reason": "expired_or_undelivered_sampling",
                #    "amount":-70000,
                #    "comment":"Deuda pendiente",
                #    "orderId":0
                #    }
                #],
                #"user":"delymar.rodriguez@rappi.com",
                #"user_id":3778
                #}'
                
                return render_template("inversions.html", im_rt=im_rt, date=goodDate, error_inv=False)

            return render_template("inversions.html", im_rt=im_rt, date=goodDate)

        currentUser = User.query.filter_by(email=username).first()
        if request.method == "POST":
            cash = request.form['cash']

            try:
                newInv = Inversion(budget=cash, owner=currentUser)
                newInv.save()
            except:
                # Pass this error if the inversion object not is created
                return render_template("inversions.html", error_inv=True, date=goodDate, data_user=currentUser)
            # If pass the creation
            return render_template("inversions.html", error_inv=False, date=goodDate, data_user=currentUser)
        # If is get method
        return render_template("inversions.html", date=goodDate, data_user=currentUser)
    
    return redirect(url_for("login"))


@invest.route("/my_carter")
def inversions():
    """ My inversions """
    if 'username' in session:
        im_rt = session.get("message")
        return render_template("my_carter.html", im_rt=im_rt)
    return redirect(url_for("login"))

@invest.route("/profile", methods=['GET', 'POST'])
def profile():
    """ displays profile template """
    from models.user import User

    if 'username' in session:
        im_rt = session.get("message")
        pUser = User.query.filter_by(email=session['username']).first()

        if request.method == "POST":
            cel = request.form['phone']
            email = request.form['email']

            params = [cel, email]

            for n in params:
                if len(n) == 0:
                    return render_template("user.html", im_rt=im_rt, error_fill=True)

            pUser.update(cel, email)
            pUser.save()

            return render_template("user.html", im_rt=im_rt, error_fill=False)

        return render_template("user.html", im_rt=im_rt, user_data=pUser)
    return redirect(url_for('login'))

@invest.route("/logout")
def logout_invest():
    return redirect(url_for("logout"))
