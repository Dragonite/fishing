from app.models import User, Poll
from app import db
from flask import render_template, flash, redirect, url_for, Markup, current_app
from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
import sys
from datetime import datetime
import operator as o


def createUser(User, pwd):
    if User==None:
        print('User object is empty ')
        return False
    else:
        if User.validate()==True:
            try:
                # with app.app_context():
                User.set_password(pwd)
                db.session.add(User)
                db.session.commit()
                return True
            except:            
                print('createUser exception raised: ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))
                return False  
                # return 'createUser exception raised: ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        else:
            print( 'createUser exception raised: Mandatory data is missing' )
            return False

            # return 'createUser exception raised: Mandatory data is missing' 

def modifyUser(User):
    if User==None:
        raise ValueError('User object is empty ')
    else:
        try:
            User.lastModifiedAt=datetime.utcnow()
            db.session.add(User)
            db.session.commit()
            return True
        except:
            print('modifyUser exception raised: ' + str(sys.exc_info()[0]))
            return False


def login_time(User):
    if User.currentLogin!=None:
        User.lastLogin=User.currentLogin
        User.currentLogin=datetime.utcnow()
    else:
        User.currentLogin=datetime.utcnow()
    try:
        User.lastModifiedAt=datetime.utcnow()
        db.session.add(User)
        db.session.commit()
        return True
    except:
        print('modifyUser exception raised: ' + str(sys.exc_info()[0]))    
        return False




def archiveUser(User):
    if User==None:
        print('User object is empty ')
        return False
    else:
        if User.isAdmin:
            print('You cannot delete Admin user!!')
            return False
        else: 
            try:
                User.lastModifiedAt=datetime.utcnow()
                User.isActive=False
                db.session.commit()
                return True
            except:
                print('archiveUser exception raised: ' + str(sys.exc_info()[0]))
                return False
               

def getUserById(userId):
    user = User.query.filter_by(userId=userId).first()
    if user==None:
        print('cannot find the user with user id - ', userId)
        return False
       
    else:
        return user

def getUserByUsername(username):
    user = User.query.filter_by(username=username).first()
    if user==None:
        print('cannot find the user with username - ', username)
        return False
    else:
        return user

def getAllUsers():
    user = User.query.all()
    return user

def createPoll(Poll):
    if Poll==None:
        print('Poll object is empty')
        return False
    else:
        if Poll.validate():
            try:
                db.session.add(Poll)
                db.session.commit()
                for index in range(Poll.howManyCandidates()):
                    Poll.Candidate[index].pollId=Poll.get_id()
                    try:
                        db.session.add(Poll.Candidate[index])
                        db.session.commit()
                    except: 
                        return 'create candidate exception raised: '+ str(sys.exc_info()[0])
                return True
            except:
                return 'createPoll exception raised: '+ str(sys.exc_info()[0])
        else:
           print('Mandatory data for a poll missing')
           return False

def modifyPoll(Poll):
    if Poll==None:
        print('Poll object is empty')
        return False
    else:
        try:
            Poll.lastModifiedAt=datetime.utcnow()
            db.session.commit()
            return True
        except:
            print('modifyPoll exception raised: ' + str(sys.exc_info()[0]))
            return False

def archivePoll(Poll):

    if Poll.isClosed:
        try:
            Poll.lastModifiedAt=datetime.utcnow()
            Poll.isActive=False
            db.session.commit()
            return True
        except:
            print('archivePoll exception raised: ' + str(sys.exc_info()[0]))
            return False
           
    elif Poll==None:
        print('Poll object is empty')
        return False
        # raise ValueError
    else: 
        print(('You need to close this poll before you delete'))
        # raise ValueError
        return False

def getPollById(pollId):
    poll=Poll.query.filter_by(pollId=pollId).first() 
    if poll==None:
        print('There is no poll with poll ID:', pollId)
        return None
        # raise ValueError
    else:
        poll.Candidate=Poll.Candidate.query.filter_by(pollId=poll.pollId).all()
        poll.Response=Poll.Response.query.filter_by(pollId=poll.pollId).all()
    return poll

def getAllPolls():
    poll=Poll.query.all()
    noPoll=len(poll)
    for index in range(noPoll):
        poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
        poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
    return poll

def getClosedPolls(isAdmin=False):
    if isAdmin:
        poll=Poll.query.filter(Poll.completedAt.isnot(None)).all()
        noPoll=len(poll)
        for index in range(noPoll):
            poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
            poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
        return poll
    else:
        poll=Poll.query.filter(Poll.completedAt.isnot(None)).filter_by(isActive=1).all()
        noPoll=len(poll)
        for index in range(noPoll):
            poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
            poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
        return poll

def getCurrentPolls(isAdmin=False):
    if isAdmin:
        poll=Poll.query.filter_by(completedAt=None).all()
        noPoll=len(poll)
        for index in range(noPoll):
            poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
            poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
        return poll
    else:
        poll=Poll.query.filter_by(completedAt=None).filter_by(isActive=1).all()
        noPoll=len(poll)
        for index in range(noPoll):
            poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
            poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
        return poll

def archiveResponse(Poll, userId):
    if Poll!=None:
        noResponses=Poll.howManyResponses()*Poll.howManyCandidates()
        for index in range(noResponses):
            if Poll.Response[index].userId==userId:
                Poll.Response[index].isActive=0
                try:
                    db.session.add( Poll.Response[index])
                    db.session.commit()
                except:
                    return False
        return True
    else:
        return False
        