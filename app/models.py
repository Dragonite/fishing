from datetime import datetime
from datetime import timedelta  
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum



@login.user_loader
def load_user(userId):
    return User.query.get(int(userId))
class User(UserMixin, db.Model):
    
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    

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

    #################################################################
    

    ################### User method definition ######################
    def __init__(self):
        self.createdAt=datetime.utcnow()
        self.lastModifiedAt=None
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
               
        self.createdByUserId=User.userId
        self.createdAt=datetime.utcnow()
        self.isActive=1
    
    def howManyCandidates(self):
        return len(self.Candidate)

    def howManyResponses(self):
        return len(self.Response)
    
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
                candidate.pollId=self.get_id()
                candidate.isActive=True
                self.Candidate.append(candidate)
                

    def getCandidateId(self, key):
        for item in self.Candidate:
            if item.candidateDescription == key:
                return item.candidateId

    def createResponse(self, userId, candidateId, preference):
        response=Poll.Response()
        response.userId=userId
        response.candidateId=candidateId
        response.response=preference
        response.createdAt=datetime.utcnow()
        return response
    
    def addResponse(self, User, candidateXresponses):
        for key, value in candidateXresponses:
             self.Responses.append(createResponse(User.userId, candidateId, value))


    
    






           

