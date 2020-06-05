#!/usr/bin/env python3
"""
Create the common found
"""
from app_flask import db
from datetime import datetime

class CommonFound(db.Model):
    """Create the found"""
    __tablename__ = "commonfound"

    id = db.Column(db.Integer, primary_key=True)
    total_money = db.Column(db.Integer, nullable=False, default=0)
    debt_money = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self):
        """Create the Found"""
        self.total_money = 0
        self.debt_money = 0

    def __repr__(self):
        """Send the information"""
        return '<Commond Found: Money = {}, Debt = {} Last Update = {}>'.format(
            self.total_money, self.debt_money, self.updated_at)

    def add_inversion(self, money):
        """Add the manoy of an inversion"""
        self.total_money += money;
        self.update_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def put_debt(self, money):
        """Minus the debt"""
        self.total_money -= money
        self.debt_money += money
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()
