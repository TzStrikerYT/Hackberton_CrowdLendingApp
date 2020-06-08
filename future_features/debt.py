#!/usr/bin/env python3
"""
Create a debt to the rappitender
"""
from app_flask import db
from datetime import datetime
import uuid

class Debt(db.Model):
    """Class to create debt to a rappitender"""
    __tablename__ = "debts"

    id = db.Column(db.String(60), primary_key=True)
    debt = db.Column(db.Integer, nullable=False)
    realtive_debt = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    tasa_interes = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reason = db.Column(db.String(500))
    state = db.Column(db.String(20), nullable=False, default="In progress")

    def save(self):
        """Save the new element"""
        db.session.add(self)
        db.session.commit()

    def update_pay(self, payment):
        """Update the mountto pay"""
        self.realtive_debt -= payment
        self.updated_at = datetime.utcnow()

    def confirmation(self, tasa):
        """Put the state and the interes"""
        pass