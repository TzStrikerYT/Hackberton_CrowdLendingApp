#!/usr/bin/python3
""" Test File for user.py """
from app_flask import user
from flask import Flask
import unittest
from flask_sqlalchemy import SQLAlchemy



class test_User(unittest.TestCase):
    """ Test to check the user method """
    def setUp(self):
        """ Set the General values to start the test """
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rappilending_test:RappiLending_Test@localhost:3306/rappilending_test_db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.secret_key = 'RappiLending_Test'
        db = SQLAlchemy(app)
        self.db = db
        obj = user.User('FirstName_test', 'LastName_test', 'test@test.com', '12345678')
        setattr(obj, 'id', 1)
        self.obj = obj
        #print(self.db.__dict__.keys())
        print("------------------")
        #print(db.Query)
        
    def tearDown(self):
        """ restore all changes necesary """
        print("Proces TearDown--> Registering logs")
        pass
    
    def test_rightCount(self):
        """ Testing the right amount of attributes """
        # print(self.__dict__)
        self.assertTrue('id' in self.obj.__dict__)
        self.assertTrue('first_name' in self.obj.__dict__)
        self.assertTrue('last_name' in self.obj.__dict__)
        self.assertTrue('email' in self.obj.__dict__)
        self.assertTrue('pwd' in self.obj.__dict__)
        
    def test_createUser(self):
        """ Method to test if the user is created """
        print("Test To create a user")
        #print(self.db)
        

