#!/usr/bin/env python3
"""
Create the user of the APP
"""
from app_flask import db
from models.inversion import Inversion
from datetime import datetime

class User(db.Model):
    """Class to make the querys to the database"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow() )
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    document = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    reg_cod = db.Column(db.String(6), nullable=True)
    validated = db.Column(db.Boolean)
    #profits = db.Column(db.Integer, default=0) Create a funtion that make the payment to the profits
    inversions = db.relationship('Inversion', cascade='all,delete-orphan', backref='owner')

    def __init__(self, first_name, last_name, email, document, phone, pwd, keyGen=''):
        """Set the columns in atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.document = document
        self.phone = phone
        self.pwd = pwd
        self.reg_cod = keyGen
        self.validated = False

    def __repr__(self):
        """Return a good representation"""
        dictionary = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'pwd': self.pwd,
            'reg_cod': self.reg_cod,
            'validated': self.validated            
            }
        return dictionary

    def save(self):
        """Save the new object into the data base"""
        db.session.add(self)
        db.session.commit()

    def update(self, phone):
        """Update the information"""
        self.phone = phone
