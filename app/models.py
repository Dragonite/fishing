from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum


@login.user_loader
def load_user(username):
  return (db.session.query(User).filter(User.username==username).first())

class User(UserMixin, db.Model):
    
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    

    ################property definitions#########################

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    firstName=db.Column(db.String(64), nullable=False)
    lastName=db.Column(db.String(64))
    username=db.Column(db.String(64),nullable=False, unique=True)
    pwdHash=db.Column(db.String(128))

    email=db.Column(db.String(128), nullable=False, unique=True)

    ad_street=db.Column(db.String(64))
    ad_suburb=db.Column(db.String(64))
    ad_state=db.Column(db.String(64))
    ad_country=db.Column(db.String(64), server_default="Australia")

    
    createdAt=db.Column(db.DateTime)
    lastModifiedAt=db.Column(db.DateTime)
   
    isActive=db.Column(db.Boolean) 
    isAdmin=db.Column(db.Boolean)

    #############################################
    

    ######### method definition #################
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, pwd):
        self.pwdHash=generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.pwdHash, pwd)

    def is_committed(self):
        return self.project_id is not None
