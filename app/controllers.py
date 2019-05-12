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
            return 'archivePoll exception raised: ' + str(sys.exc_info()[0])
    elif Poll==None:
        raise ValueError('Poll object is empty')
    else: 
        raise ValueError('You need to close this poll before you delete')
        return False

def getPollById(pollId):
    poll=Poll.query.filter_by(pollId=pollId).first() 
    if poll==None:
        raise ValueError('There is no poll with poll ID:', pollId)
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

def getClosedPoll():
    poll=Poll.query.filter(Poll.completedAt.isnot(None)).all()
    noPoll=len(poll)
    for index in range(noPoll):
        poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
        poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
    return poll

def getCurrentPoll():
    poll=Poll.query.filter_by(completedAt=None).all()
    noPoll=len(poll)
    for index in range(noPoll):
        poll[index].Candidate=Poll.Candidate.query.filter_by(pollId=poll[index].pollId).all()
        poll[index].Response=Poll.Response.query.filter_by(pollId=poll[index].pollId).all()
    return poll


def getResults(Poll):
    

    def getCanIndex(canList, key):
        listLen=len(canList)
        for index in range(listLen):
            if canList[index][1]==key:
                return canList[index][0]

    def getCanList(Poll):
        CList=[]
        howManyCandidates=Poll.howManyCandidates()
        howManyResponses =Poll.howManyResponses()
        
        for candidate in Poll.Candidate:
            temp=[]
            temp.append(0)
            temp.append(candidate.candidateId)
            temp.append(candidate.candidateDescription)
            CList.append(temp)
            
        CList.sort()
        for index in range(len(CList)):
            CList[index][0]=index
        return CList

    def getResList(Poll):
        Result={}
        RList=[]
        howManyCandidates=Poll.howManyCandidates()
        howManyResponses =Poll.howManyResponses()
        for response in Poll.Response:
            if response.isActive:
                if Result.get(response.userId)==None:
                    Result[response.userId]=[]
                    for index in range(howManyCandidates):
                        Result[response.userId].append(0)
                    Result[response.userId][getCanIndex(getCanList(Poll),response.candidateId)]=response.response
                else:
                    Result[response.userId][getCanIndex(getCanList(Poll),response.candidateId)]=response.response
        for key, value in Result.items():
            RList.append(value)
        return RList
    
    def findSN(list): 
        temp=[]
        if sum(list) != 0:
            if 0 in list:
                for i in list:
                    if i!= 0:
                        temp.append(i)  
                return min(temp)
            else:
                return min(list)
        else:
            return -1


    def decision(count, totalCount, CList): 
        global msg
        result=(sorted(count, key=o.itemgetter(1), reverse=True))

        for i in range(len(result)):
            msg+=str(result[i][1])+"\t"+ str(result[i][0]) + "\n"
       
        if(len(result)<=1):
            return list(result[0]), True

        elif(totalCount==0):
            return [], False
        else:
            if (result[0][1] / totalCount) <= 0.5:
                return list(result[len(result)-1]), False
            else:
                return list(result[0]), True
        
    def prefResult( RList, CList, voteCount):
        global msg
        responseCount=len(RList)
        candidateCount=len(CList)
        count=[]
        totalCount=0
        voteCount += 1
        
        for item in CList:
            count.append([item, 0])
 
        for index in range(responseCount):
            tempindex=RList[index].index(findSN(RList[index]))
            count[tempindex][1]+=1
            totalCount+=1     
        
        results, decisionFlag = decision(count, totalCount, CList)


        if decisionFlag is False:
            if (results!=[]):
                msg += "\nCandidate " + str(CList[count.index(results)][2]) + " has the smallest number of votes and is eliminated from the count\n\n"
                del (CList[count.index(results)])
                for index in range(responseCount):
                    del (RList[index][count.index(results)])
                prefResult(RList, CList, totalCount)
            # else:
            #     return msg
        else:
            msg+="\n"+str(count[0][1])+"\t"+ str(count[0][0]) + "\n"
            msg += "\nCandidate " + str(results[0][2]) + " is elected\n"
        






    global msg
    msg=""
    CList=getCanList(Poll)
    RList=getResList(Poll)
    # voteCount=0

    prefResult(RList, CList,0)
    print("final:  ", msg)



