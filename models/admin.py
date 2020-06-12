#!/usr/bin/env python3
"""
Create the user of the APP
"""
from app_flask import db
from models.inversion import Inversion
from datetime import datetime

class Admin(db.Model):
    """Class to make the querys to the database"""
    __tablename__ = 'admins'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    credentials = db.Column(db.Integer, default=1)

    def __init__(self, first_name, last_name, username, pwd):
        """Set the columns in atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.pwd = pwd

    def save(self):
    """Save the new object into the data base"""
        db.session.add(self)
        db.session.commit()