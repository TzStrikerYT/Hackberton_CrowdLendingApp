#!/usr/bin/env python3
"""
Create the user of the APP
"""
from app_flask.login_app import db


class User(db.Model):
    """Class to make the querys to the database"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    pwd = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name, email, pwd):
        """Set the columns in atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pwd = pwd

    def __repr__(self):
        """Return a good representation"""
        return '<User {}: password = {}>'.format(self.first_name, self.pwd)

    def save(self):
        """Save the new object into the data base"""
        db.session.add(self)
        db.session.commit()

db.create_all()
