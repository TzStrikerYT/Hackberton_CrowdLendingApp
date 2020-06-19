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


    id = db.Column(db.Integer, primary_key=True)
    debt = db.Column(db.Integer, nullable=False) # Total de la deuda
    realtive_debt = db.Column(db.Float, default=0) #Deuda disminuida a capital
    
    interest_rate = db.Column(db.Float, default=0) # Tasa de interes
    fee_payment = db.Column(db.Integer, default=0) # Cantidad de cuotas pactadas
    fee_value = db.Column(db.Float, default=0) # Valor de la cuota
    actual_fee_payment = db.Column(db.Integer, default=0) # Cuotas pagadas
    #fee_state = db.Column(db.Boolean)

    capital_pay = db.Column(db.Float, default=0)
    interest_pay = db.Column(db.Float, default=0)
    
    reason = db.Column(db.String(500)) # Razon de la peticion del prestamo
    state = db.Column(db.String(20), nullable=False, default="In progress") # Estado del prestamo
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

    def save(self):
        """Save the new element"""
        
        db.session.add(self)
        db.session.commit()
    
    
    def update_pay(self, payment):
        """Update the mountto pay"""
        
        if payment == self.fee_value:
            self.interest_pay = self.interest_rate / self.realtive_debt
            print("Este es el interes", self.interest_pay)
            print(self.fee_value)
            self.capital_pay = self.fee_value - self.interest_pay
            print(self.capital_pay)

            self.realtive_debt -= self.capital_pay
            self.updated_at = datetime.utcnow()
            self.actual_fee_payment += 1

        else:
            return "La el valor cuota es incorrecta"
    
    
    def confirmation(self, confirm, rate=0, fee_payment=0):
        """Put the state and the interes"""
        
        if confirm == "postulated":
            self.state = "Postulated"
            self.interest_rate = rate
            self.fee_payment = fee_payment
            goodRate = rate / 100

            # Valor de la cuota (formula de interes compuesto)
            self.fee_value = (goodRate * self.debt) / (1 - (pow(1 + goodRate, (self.fee_payment * -1))))
            print(self.fee_value)

        if confirm == "rejected":
            self.state = "Rejected"

        if confirm == "accepted":
            self.realtive_debt = self.debt
            self.state = "Accepted"

        if confirm == "payed":
            self.state = "Payed"