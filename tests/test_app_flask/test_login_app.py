#/usr/bin/python3
""" Test for Login_app function"""
import unittest
from app_flask.login_app import app

class Test_login_app(unittest.TestCase):
    """ Class to test the login system """
    def setUp(self):
        """ SetUp Method """
        app.config['TESTING'] = True
        app.config['DEBU'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rappilending_test:RappiLending_Test@localhost:3306/rappilending_test_db'
        tester =  app.test_client(self)
    
    def tearDown(self):
        """ TearDown """
        pass

    def test_notFound(self):
        """ The correct no found page """
        tester =  app.test_client(self)
        res = tester.get('/not_found', content_type='html/text')
        self.assertEqual(res._status_code, 404)
#        print(res._status_code)

    def test_correctLogin(self):
        """ chech response correct login """
        tester =  app.test_client(self)
        res = tester.get('/login', content_type='html/text')
        res2 =  tester.get('/', content_type='html/text')
        self.assertEqual(res._status_code, 200)
        self.assertEqual(res._status_code, 200)
        res = tester.post('/login', data=dict(username='test_user', password='test_pwd'))
        
    
    def test_wrongCredentials(self):
        """ Check the response of wrong credentials """
        tester = app.test_client(self)

        