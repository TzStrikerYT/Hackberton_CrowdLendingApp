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
    print("esta es mi session", session)
    if "username" in session:
        return "this is the aplication to create a new inversion", 200

    return redirect(url_for("login"))


@invest.route("/my_inversions")
def inversions():
    """My inversions"""
    return "My inversion", 200


@invest.route("/logout")
def logout_invest():
    return redirect(url_for("logout"))
