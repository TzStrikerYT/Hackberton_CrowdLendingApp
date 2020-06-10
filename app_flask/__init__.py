#!/usr/bin/env python3
from flask import Flask
from app_flask.invest_app import invest
from flask_sqlalchemy import SQLAlchemy

# Creacion de la API
app = Flask(__name__)
app.register_blueprint(invest, url_prefix="/invest")

# Coneccion con la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/rappilending_dev_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'esto-es-una-clave-secreta'

from models.user import User
from models.inversion import Inversion
from models.commonFound import CommonFound

db.create_all()
