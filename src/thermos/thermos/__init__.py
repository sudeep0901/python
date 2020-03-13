
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from logging import DEBUG
from thermos import models
from thermos import views

print("Running init")
app = Flask(__name__)
app.logger.setLevel(DEBUG)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = b'<\xfbx~te\x06\xcc2,+\x85\x15^\xec\x85\xe8\xd6\xf5\x8eC?\xbfB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
