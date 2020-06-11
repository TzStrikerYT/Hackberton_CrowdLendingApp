#!/usr/bin/env python3
"""
Create an inversion
"""
from app_flask import db
from datetime import datetime
import uuid

class Inversion(db.Model):
    """
    class to create an inversion
    """
    __tablename__ = 'inversions'

    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    #rappi_points = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        """Return a representacion"""
        return '<Inversion {}: created at {}>'.format(self.budget, self.created_at)

    def save(self):
        """Save the new element"""
        db.session.add(self)
        db.session.commit()
