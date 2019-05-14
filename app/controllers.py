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
        raise ValueError('User object is empty ')
    else:
        if User.validate():
            
            try:
                # with app.app_context():
                User.set_password(pwd)
                db.session.add(User)
                db.session.commit()
                User.get_token()
                return True
            except:      
                return 'createUser exception raised: ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        else:
            return 'createUser exception raised: Mandatory data is missing' 

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
            return 'modifyUser exception raised: ' + str(sys.exc_info()[0])



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
    except:
        return 'modifyUser exception raised: ' + str(sys.exc_info()[0])    




def archiveUser(User):
    if User==None:
        raise ValueError('User object is empty ')
    else:
        if User.isAdmin:
            raise ValueError('You cannot delete Admin user!!')
            return False
        else: 
            try:
                User.lastModifiedAt=datetime.utcnow()
                User.isActive=False
                db.session.commit()
                return True
            except:
                return 'archiveUser exception raised: ' + str(sys.exc_info()[0])

def getUserById(userId):
    user = User.query.filter_by(userId=userId).first()
    if user==None:
        raise ValueError('cannot find the user with user id - ', userId)
    else:
        return user

def getUserByUsername(username):
    user = User.query.filter_by(username=username).first()
    if user==None:
        raise ValueError('cannot find the user with username - ', username)
    else:
        return user

def getAllUsers():
    user = User.query.all()
    return user

def createPoll(Poll):
    if Poll==None:
        raise ValueError('Poll object is empty')
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
            raise ValueError('Mandatory data for a poll missing')

def modifyPoll(Poll):
    if Poll==None:
        raise ValueError('Poll object is empty')
    else:
        try:
            Poll.lastModifiedAt=datetime.utcnow()
            db.session.commit()
            return True
        except:
            return 'modifyPoll exception raised: ' + str(sys.exc_info()[0])

def archivePoll(Poll):

    if Poll.isClosed:
        try:
            Poll.lastModifiedAt=datetime.utcnow()
            Poll.isActive=False
            db.session.commit()
            return True
        except:
            return False
            # return 'archivePoll exception raised: ' + str(sys.exc_info()[0])
    elif Poll==None:
        return False
        # raise ValueError('Poll object is empty')
    else: 
        # raise ValueError('You need to close this poll before you delete')
        return False

def getPollById(pollId):
    poll=Poll.query.filter_by(pollId=pollId).first() 
    if poll==None:
        return None
        # raise ValueError('There is no poll with poll ID:', pollId)
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
        noResponses=Poll.howManyResponses()
        for index in range(noResponses):
            if Poll.Response[index].userId==userId:
                Poll.Response[index].isActive=0
                try:
                    db.session.commit()
                    return True
                except:
                    return False
    else:
        return False
        