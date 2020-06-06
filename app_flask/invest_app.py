#!/usr/bin/env python3
"""
The flow to investor
"""
from flask import (
    Blueprint, render_template,
    session, redirect, url_for)

#from models import inversion

invest = Blueprint("invest", __name__)

@invest.route("/new_inversion")
def home_investe():
    """Create a new inversionobject"""
    im_rt = session.get("message")
    if "username" in session:
        return render_template("inversions.html", im_rt=im_rt)

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
