from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum

class user(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    firstName=db.Column(db.String(64), nullable=False)
    lastName=db.Column(db.String(64))
    logInId=db.Column(db.String(64))
    pwdHash=db.Column(db.String(128))

    email=db.Column(db.String(128), nullable=False, unique=True)

    ad_street=db.Column(db.String(64))
    ad_suburb=db.Column(db.String(64))
    ad_state=db.Column(db.String(64))
    ad_country=db.Column(db.String(64), server_default="Australia")

    
    createdAt=db.Column(db.DateTime)
    lastModifiedAt=db.Column(db.DateTime)
   
    isActive=db.Column(Enum('true','false')) 
    isAdmin=db.Column(Enum('true','false'))
