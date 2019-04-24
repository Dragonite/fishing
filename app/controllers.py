from app.models import User, Poll
from app import app, db
from flask import render_template, flash, redirect, url_for, Markup
from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
import sys
from datetime import datetime

def createUser(User, pwd):
    try:
        User.set_password(pwd)
        db.session.add(User)
        db.session.commit()
        return True
    except:      
        return sys.exc_info()[0]
def modifyUser(User):
    try:
        User.lastModifiedAt=datetime.utcnow()
        db.session.commit()
        return True
    except:
        return sys.exc_info()[0]
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
        return sys.exc_info()[0]

def archivePoll(Poll):
    if Poll.isClosed:
        try:
            Poll.lastModifiedAt=datetime.utcnow()
            Poll.isActive=False
            db.session.commit()
            return True
        except:
            return sys.exc_info()[0]
    else: 
        raise ValueError('You need to close this poll before you delete')
        return False

