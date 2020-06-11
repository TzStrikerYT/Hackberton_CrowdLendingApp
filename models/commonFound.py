#!/usr/bin/env python3
"""
Create the common found
"""
from app_flask import db
from datetime import datetime
import csv

class CommonFound(db.Model):
    """Create the found"""
    __tablename__ = "commonfound"

    id = db.Column(db.Integer, primary_key=True)
    total_money = db.Column(db.Integer, nullable=False, default=0)
    debt_money = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    profits = db.Column(db.Integer, default=0)

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
        # add in DB
        self.total_money += money
        self.update_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

        # Put the history in a file
        empty = True
        date = datetime.utcnow()
        goodDate = date.strftime('%d-%m-%Y')

        try:
            with open("found_history.csv") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                print(csv_reader)

                #if len(csv_reader) > 0:
                    #empty = False
        except FileNotFoundError:
                with open("found_history.csv", "w", newline="", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Change Date", "Total Money", "Debt Money", "Type Change", "Change Value"])
        
        with open("found_history.csv", "a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([goodDate, self.total_money, self.debt_money, "Inversion", money])


    def put_debt(self, money):
        """Minus the debt"""
        self.total_money -= money
        self.debt_money += money
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()
