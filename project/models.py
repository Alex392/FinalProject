from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, String, MetaData

from .app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class functions(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    userName = db.Column(db.String(1000))
    functionName = db.Column(db.String(1000))
    numbers = db.Column(db.String(1000))
