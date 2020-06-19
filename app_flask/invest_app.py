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
    from models.commonFound import CommonFound
    from models.debt import Debt

    # Make code for both type users
    im_rt = session.get('message')
    if "username" in session:
        username = session.get('username')
        date = datetime.utcnow()
        goodDate = date.strftime('%d-%m-%Y')

        currentUser = User.query.filter_by(email=username).first()
        debts = []

        for debt in currentUser.debts:
            if debt.state != "Payed":
                debts.append(debt)

        if im_rt is True:
            #Add here the code for generate debt with the API
            if request.method == "POST":
                if len(debts) >= 1:
                    return render_template("inversions.html", im_rt=im_rt, date=goodDate, error_maxDebt=True)#Have a debt whitout pay, so the person can't make a new debt

                the_debt = request.form['cash']
                reason = request.form['motive']

                new_debt = Debt(debt=the_debt, reason=reason, owner=currentUser)                    
                new_debt.save()
                
                return render_template("inversions.html", im_rt=im_rt, date=goodDate, error_inv=False)

            return render_template("inversions.html", im_rt=im_rt, date=goodDate)


        if request.method == "POST":
            cash = request.form['cash']

            try:
                newInv = Inversion(budget=cash, owner=currentUser)
                newInv.save()
            except:
                # Pass this error if the inversion object not is created
                return render_template("inversions.html", error_inv=True, date=goodDate, data_user=currentUser)

            found = CommonFound.query.first()
            print(found)
            if found is None:
                found = CommonFound()

            found.add_inversion(newInv.budget)

            # If pass the creation
            return render_template("inversions.html", error_inv=False, date=goodDate, data_user=currentUser)
        # If is get method
        return render_template("inversions.html", date=goodDate, data_user=currentUser)
    
    return redirect(url_for("login"))


@invest.route("/my_carter", methods=['GET', 'POST'])
def inversions():
    """ My inversions """
    from models.user import User

    if 'username' in session:
        im_rt = session.get("message")
        date = datetime.utcnow()
        goodDate = date.strftime('%d-%m-%Y')

        currentUser = User.query.filter_by(email=session['username']).first()
        debt = currentUser.debts[0]

        if request.method =="POST":
            pay = float(request.form['monto'].replace(",", "."))
            if debt.realtive_debt == 0:
                debt.confirmation("payed")
                debt.save()
                return render_template("my_carter.html", im_rt=im_rt, date=goodDate, debt=debt, errorPayed=True)#Your debt is already payed

            if debt.state == "Accepted":
                status = debt.update_pay(pay)
                if status == "La el valor cuota es incorrecta":
                    return render_template("my_carter.html", im_rt=im_rt, date=goodDate, debt=debt, errorValue=True)#When pay a value that not is the same that the fee that must pay
                debt.save()

            return render_template("my_carter.html", im_rt=im_rt, date=goodDate, debt=debt, errorAccept=True) #This error say that not pay an debt that no are accepted yet

        return render_template("my_carter.html", im_rt=im_rt, date=goodDate, debt=debt)
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

            if len(cel) == 0:
                return render_template("user.html", im_rt=im_rt, error_fill=True, user_data=pUser)

            pUser.update(cel)
            pUser.save()

            return render_template("user.html", im_rt=im_rt, error_fill=False, user_data=pUser)

        return render_template("user.html", im_rt=im_rt, user_data=pUser)
    return redirect(url_for('login'))

@invest.route("/logout")
def logout_invest():
    return redirect(url_for("logout"))
