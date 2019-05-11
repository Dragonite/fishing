from datetime import datetime
from datetime import timedelta  
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
import sys
import pycountry
import base64
import os

from flask import url_for


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data           
@login.user_loader
def load_user(userId):
    return User.query.get(int(userId))

class User(PaginatedAPIMixin, UserMixin, db.Model):
    
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    

    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    
    
    ################User property definitions#########################

    userId=db.Column(db.Integer, primary_key=True, autoincrement=True)
    
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

    lastLogin=db.Column(db.DateTime)
    currentLogin=db.Column(db.DateTime)
    #################################################################
    

    ################### User method definition ######################
    def __init__(self):
        self.createdAt=datetime.utcnow()
        self.lastModifiedAt=None
        self.lastLoginAt=None
        self.isActive=True
        self.isAdmin=False
    
    def validate(self):
        if self.firstName and self.lastName and self.email:
            return True
        else:
            return False
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, pwd):
        self.pwdHash=generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.pwdHash, pwd)

    def get_id(self):
            return(self.userId)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token
    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def to_dict(self, include_email=False, as_admin=False):
        data = {
            'userId': self.userId,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'ad_street':self.ad_state,
            'ad_suburb':self.ad_suburb,
            'ad_state':self.ad_state,
            'ad_country':self.ad_country,
            'ad_country_code': pycountry.countries.get(name=self.ad_country).alpha_2.lower(),
            'lastLogin':self.lastLogin,
            'currentLogin':self.currentLogin,
            'token': self.token,
            'token_expiration': self.token_expiration 
        }
        if include_email:
            data['email'] = self.email
        if as_admin:
            data['createdAt']=self.createdAt
            data['lastModifiedAt']=self.lastModifiedAt
            data['isActive']=self.isActive
            data['isAdmin']=self.isAdmin
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email','firstName','lastName','ad_street', 'ad_suburb','ad_state','token','token_expiration', ]:
            if field in data:
                setattr(self, field, data[field]) ###############################################
        if new_user and 'password' in data:
            self.set_password(data['password'])


class Poll(db.Model):
    
    __tablename__ = 'polls'
    __table_args__ = {'sqlite_autoincrement': True}

    ################Poll property definitions#########################
    pollId=db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    title=db.Column(db.String(64), nullable=False, unique=True)
    description=db.Column(db.String(250))

    createdAt=db.Column(db.DateTime)
    lastModifiedAt=db.Column(db.DateTime)
    completedAt=db.Column(db.DateTime)

    orderCandidatesBy=db.Column(Enum('Desc','Acs','SpecialOrder'))
    minResponses=db.Column(db.Integer)
    openAt=db.Column(db.DateTime)
    closeAt=db.Column(db.DateTime)

    createdByUserId=db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)

    isOpenPoll=db.Column(db.Boolean) 
    isActive=db.Column(db.Boolean) 

    class Candidate(db.Model):
        
        __tablename__ = 'candidates'
        __table_args__ = (db.UniqueConstraint('pollId', 'candidateDescription', name='unique_candidates'),{'sqlite_autoincrement': True})

        candidateId=db.Column(db.Integer, primary_key=True, autoincrement=True)
        candidateDescription=db.Column(db.String(128), nullable=False)
        displayOrder=db.Column(db.Integer)
        isActive=db.Column(db.Boolean) 
        pollId=db.Column(db.Integer, db.ForeignKey('polls.pollId'), nullable=False)
        
        def get_id(self):
            return(self.candidateId)


    class Response(db.Model):

        __tablename__ = 'responses'
        __table_args__ = (db.UniqueConstraint('userId', 'pollId', 'candidateId', 'response', name='unique_resonses'),{'sqlite_autoincrement': True})

        responseId=db.Column(db.Integer, primary_key=True, autoincrement=True)
        userId=db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
        pollId=db.Column(db.Integer, db.ForeignKey('polls.pollId'), nullable=False)
        candidateId=db.Column(db.Integer, db.ForeignKey('candidates.candidateId'), nullable=False)
        
        isActive=db.Column(db.Boolean)
        response=db.Column(db.Integer)
        createdAt=db.Column(db.DateTime)

        def get_id(self):
            return(self.responseId)

        def validate(self):   
            if userId and pollId and candidateId:
                return True
            else:
                return False
    ################### Poll method definition ######################
    def __init__(self, title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, User):
        self.Candidate=self.Candidate()
        self.Candidate=[]

        self.Response=self.Response()
        self.Response=[]

        self.lastModifiedAt=None
        self.completedAt=None
        self.title=title
        self.description=description
        
        if minResponses>0:
            self.minResponses=minResponses
        else:
            self.minResponses=-1
        
        if orderCandidatesBy==None:
            self.orderCandidatesBy='Acs'
        else:
            self.orderCandidatesBy=orderCandidatesBy

        if isOpenPoll==None:
            self.isOpenPoll=False
        else:
            self.isOpenPoll=isOpenPoll
        
        if openAt==None:
            self.openAt=datetime.utcnow()
        else:
            self.openAt=openAt
        
        if closeAt==None:
            self.closeAt=datetime.utcnow()+timedelta(days=7)
        else:
            self.closeAt=closeAt
        try:
            self.createdByUserId=User.userId
        except:
             raise ValueError('User object is empty')
        self.createdAt=datetime.utcnow()
        self.isActive=1
    
    def howManyCandidates(self):
        if self.Candidate == None:
            return 0
        else:
            return len(self.Candidate)

    def howManyResponses(self):
        if self.Response==None:
            return 0
        elif self.Candidate==None:
             raise ValueError('There is no candidate saved yet')
        else:
            return int(len(self.Response)/self.howManyCandidates())
    
    def close(self):
        self.completedAt=datetime.utcnow()
    
    def isClosed(self):
        if self.completedAt:
            return True
        else:
            return False

    def validate(self):    
        if self.title and self.orderCandidatesBy and self.createdByUserId and self.howManyCandidates()>0:
            return True
        else: 
            return False
    
    def get_id(self):
            return(self.pollId)

    def addCandidate(self, candidateDescription, displayOrder):
        if candidateDescription==None:
             raise ValueError('You must enter the candidate details!')
        else:
            if self.orderCandidatesBy=='SpecialOrder' and displayOrder==None:
                raise ValueError('You must enter the order you want to display this candidate!')
            else:
                candidate = Poll.Candidate()
                candidate.candidateDescription=candidateDescription
                candidate.displayOrder=displayOrder
                # if self.get_id() != None:
                #     candidate.pollId=self.get_id()
                # else: 
                #      raise ValueError('Poll needs to be commited to DB before add candidate')
                candidate.isActive=True
                self.Candidate.append(candidate)
                

    def getCandidateId(self, key):
        for item in self.Candidate:
            if item.candidateDescription == key:
                return item.candidateId

    def addResponse(self, userId, preferenceXresponses):
        if self.isClosed():
            raise ValueError('This poll has been closed since ', Poll.completedAt)
            return False
        else:
            if preferenceXresponses==None:
                raise ValueError('You must enter preference order for each option')
                return False
            else:
                for key, value in preferenceXresponses.items():
                    response=Poll.Response()
                    response.userId=userId
                    response.pollId=self.pollId
                    response.candidateId=key
                    response.response=value
                    response.createdAt=datetime.utcnow()
                    response.isActive=True
                    self.Response.append(response)
                    try:
                        db.session.add(response)
                        db.session.commit()
                    except: 
                        return 'addResponse exception raised: '+ str(sys.exc_info()[0])
            return True

    def to_dict(self, as_admin=False):
        data = {
            'userId': self.userId,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'ad_street':self.ad_state,
            'ad_suburb':self.ad_suburb,
            'ad_state':self.ad_state,
            'ad_country':self.ad_country,
            'ad_country_code': pycountry.countries.get(name=self.ad_country).alpha_2.lower(),
            'lastLogin':self.lastLogin,
            'currentLogin':self.currentLogin
        }
        if as_admin:
            data['createdAt']=self.createdAt
            data['lastModifiedAt']=self.lastModifiedAt
            data['isActive']=self.isActive
            data['isAdmin']=self.isAdmin
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email','firstName','lastName','ad_street', 'ad_suburb','ad_state']:
            if field in data:
                setattr(self, field, data[field]) ###############################################
        if new_user and 'password' in data:
            self.set_password(data['password'])