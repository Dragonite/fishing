from app.models import User, Poll
from app import app, db
from flask import render_template, flash, redirect, url_for, Markup
from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
import sys
from datetime import datetime

def createUser(User, pwd):
    if User.validate():
        try:
            User.set_password(pwd)
            db.session.add(User)
            db.session.commit()
            return True
        except:      
            return 'createUser exception raised: ' + sys.exc_info()[0]
    else:
        return 'createUser exception raised: Mandatory data is missing' 

def modifyUser(User):
    try:
        User.lastModifiedAt=datetime.utcnow()
        db.session.commit()
        return True
    except:
        return 'modifyUser exception raised: ' +sys.exc_info()[0]

def archiveUser(User):
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
            return 'archiveUser exception raised: ' + sys.exc_info()[0]

def getUserById(userId):
    user = User.query.filter_by(userId=userId).first()
    return user

def getUserByUsername(username):
    user = User.query.filter_by(username=username).first()
    return user


def createPoll(Poll):
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
    try:
        Poll.lastModifiedAt=datetime.utcnow()
        db.session.commit()
        return True
    except:
        return 'modifyPoll exception raised: ' + sys.exc_info()[0]

def archivePoll(Poll):
    if Poll.isClosed:
        try:
            Poll.lastModifiedAt=datetime.utcnow()
            Poll.isActive=False
            db.session.commit()
            return True
        except:
            return 'archivePoll exception raised: ' + sys.exc_info()[0]
    else: 
        raise ValueError('You need to close this poll before you delete')
        return False

def getPollById(pollId):
    poll=Poll.query.filter_by(pollId=pollId).first() 
    poll.Candidate=Poll.Candidate.query.filter_by(pollId=poll.pollId).all()
    poll.Response=Poll.Response.query.filter_by(pollId=poll.pollId).all()
    return poll




def getResults(Poll):
    results={}
    return results



# def createResponse(userId, preferenceXresponses):
#     responses=Poll.Response()
#     responses=[]
#     if preferenceXresponses==None:
#         raise ValueError('You must enter preference order for each option')
#         return False
#     else:
#         for key, value in preferenceXresponses.items():
#             response=Poll.Response()
#             response.userId=userId
#             response.candidateId=key
#             response.response=value
#             response.createdAt=datetime.utcnow()
#             response.isActive=True
#             responses.append(response)
#     if responses:
#         return responses
#     else:
#         return False

# def addResponse(Poll, responses):
#     if Poll.isClosed():
#          raise ValueError('This poll has been closed since ', Poll.completedAt)
#     else:

#         for item in responses:
#             try:
#                 db.session.add(item)
#                 db.session.commit()
#             except: 
#                 return 'addResponse exception raised: '+ str(sys.exc_info()[0])