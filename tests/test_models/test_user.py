#!/usr/bin/python3
""" Test File for user.py """
from app_flask.user import User
from flask import Flask, session
import unittest
from flask_sqlalchemy import SQLAlchemy
import uuid
import random
import string


class test_User(unittest.TestCase):
    """ Test to check the user method """
    def setUp(self):
        """ Set the General values to start the test """
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rappilending_dev:RappiLending_Dev@localhost:3306/rappilending_dev_db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.secret_key = 'RappiLending_Test'
        db = SQLAlchemy(app)
        mail = ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + '@email.com'
        self.db = db
        obj = User('FirstName_test', 'LastName_test', mail, '12345678')
        self.obj = obj
        
    def tearDown(self):
        """ restore all changes """
        pass
    
    def test_rightCount(self):
        """ Testing the right amount of attributes """
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'pwd'))
        
    def test_SaveUser(self):
        """ Method to test if the user is created and saved"""
        self.obj.save()
        records = self.db.session.query(User).all()
        for usr in records:
            print(usr.email)
            if usr.email == self.obj.email:
                saved = True
                break
        self.db.session.query(User).filter(User.email == self.obj.email).delete()
        self.db.session.commit()
        self.assertTrue(saved);
        
        

            
