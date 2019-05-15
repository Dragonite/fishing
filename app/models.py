import base64
import json
import operator as o
import os
import sys
from datetime import datetime
from datetime import timedelta

import pycountry
from flask import url_for
from flask_login import UserMixin
from sqlalchemy import Enum
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


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

    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)

    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64))
    username = db.Column(db.String(64), nullable=False, unique=True)
    pwdHash = db.Column(db.String(128))

    email = db.Column(db.String(128), nullable=False, unique=True)

    ad_street = db.Column(db.String(64))
    ad_suburb = db.Column(db.String(64))
    ad_state = db.Column(db.String(64))
    ad_country = db.Column(db.String(64), server_default="Australia")

    createdAt = db.Column(db.DateTime)
    lastModifiedAt = db.Column(db.DateTime)

    isActive = db.Column(db.Boolean)
    isAdmin = db.Column(db.Boolean)

    lastLogin = db.Column(db.DateTime)
    currentLogin = db.Column(db.DateTime)

    #################################################################

    ################### User method definition ######################
    def __init__(self):
        self.createdAt = datetime.utcnow()
        self.lastModifiedAt = None
        self.lastLoginAt = None
        self.isActive = True
        self.isAdmin = False

    def validate(self):
        if self.username and self.firstName and self.email:
            return True
        else:
            return False

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, pwd):
        self.pwdHash = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.pwdHash, pwd)

    def get_id(self):
        return (self.userId)

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

    def howManyResponses(self):
        responses = Poll.Response.query.filter_by(userId=self.userId).all()
        polls = []
        current = None
        totalResponses = 0
        pollIds = []

        for item in responses:
            if current == item.pollId:
                pass
            else:
                current = item.pollId
                pollIds.append(current)
                totalResponses += 1
        returnData = {
            'userId': self.userId,
            'totalResponses': totalResponses,
            'pollIds': pollIds
        }
        return responses, returnData

    def howManyPolls(self):
        poll = Poll.query.filter_by(createdByUserId=self.userId).all()
        return (poll)

    def to_dict(self, include_email=False, as_admin=False):
        data = {
            'userId': self.userId,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'ad_street': self.ad_state,
            'ad_suburb': self.ad_suburb,
            'ad_state': self.ad_state,
            'ad_country': self.ad_country,
            'ad_country_code': pycountry.countries.get(name=self.ad_country).alpha_2.lower(),
            'lastLogin': self.lastLogin,
            'currentLogin': self.currentLogin,
            'token': self.token,
            'token_expiration': self.token_expiration
        }
        if include_email:
            data['email'] = self.email
        if as_admin:
            data['createdAt'] = self.createdAt
            data['lastModifiedAt'] = self.lastModifiedAt
            data['isActive'] = self.isActive
            data['isAdmin'] = self.isAdmin
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'firstName', 'lastName', 'ad_street', 'ad_suburb', 'ad_state', 'token',
                      'token_expiration', ]:
            if field in data:
                setattr(self, field, data[field])  ###############################################
        if new_user and 'password' in data:
            self.set_password(data['password'])


class Poll(PaginatedAPIMixin, db.Model):
    __tablename__ = 'polls'
    __table_args__ = {'sqlite_autoincrement': True}

    ################Poll property definitions#########################
    pollId = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(250))

    createdAt = db.Column(db.DateTime)
    lastModifiedAt = db.Column(db.DateTime)
    completedAt = db.Column(db.DateTime)

    orderCandidatesBy = db.Column(Enum('Desc', 'Acs', 'SpecialOrder'))
    minResponses = db.Column(db.Integer)
    openAt = db.Column(db.DateTime)
    closeAt = db.Column(db.DateTime)

    createdByUserId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)

    isOpenPoll = db.Column(db.Boolean)
    isActive = db.Column(db.Boolean)

    class Candidate(db.Model):

        __tablename__ = 'candidates'
        __table_args__ = (
        db.UniqueConstraint('pollId', 'candidateDescription', name='unique_candidates'), {'sqlite_autoincrement': True})

        candidateId = db.Column(db.Integer, primary_key=True, autoincrement=True)
        candidateDescription = db.Column(db.String(128), nullable=False)
        displayOrder = db.Column(db.Integer)
        isActive = db.Column(db.Boolean)
        pollId = db.Column(db.Integer, db.ForeignKey('polls.pollId'), nullable=False)

        def get_id(self):
            return (self.candidateId)

        def to_dict(self):
            data = {
                'candidateDescription': self.candidateDescription,
                'displayOrder': self.displayOrder,
                'pollId': self.pollId,
                'candidateId': self.candidateId,
                'isActive': self.isActive
            }
            return data

        def from_dict(self, data):
            for field in ['pollId', 'displayOrder', 'candidateId', 'isActive', 'candidateDescription']:
                if field in data:
                    setattr(self, field, data[field])

    class Response(db.Model):

        __tablename__ = 'responses'
        __table_args__ = (db.UniqueConstraint('userId', 'pollId', 'candidateId', 'response', name='unique_resonses'),
                          {'sqlite_autoincrement': True})

        responseId = db.Column(db.Integer, primary_key=True, autoincrement=True)
        userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
        pollId = db.Column(db.Integer, db.ForeignKey('polls.pollId'), nullable=False)
        candidateId = db.Column(db.Integer, db.ForeignKey('candidates.candidateId'), nullable=False)

        isActive = db.Column(db.Boolean)
        response = db.Column(db.Integer)
        createdAt = db.Column(db.DateTime)

        def get_id(self):
            return (self.responseId)

        def validate(self):
            if userId and pollId and candidateId:
                return True
            else:
                return False

        def to_dict(self):
            data = {
                'responseId': self.responseId,
                'userId': self.userId,
                'pollId': self.pollId,
                'candidateId': self.candidateId,
                'isActive': self.isActive,
                'response': self.response,
                'createdAt': self.createdAt,
            }
            return data

        def from_dict(self, data):
            for field in ['pollId', 'userId', 'candidateId', 'isActive', 'response', 'createdAt']:
                if field in data:
                    setattr(self, field, data[field])

    ################### Poll method definition ######################
    def __init__(self, title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, User):
        self.Candidate = self.Candidate()
        self.Candidate = []

        self.Response = self.Response()
        self.Response = []

        self.lastModifiedAt = None
        self.completedAt = None
        self.title = title
        self.description = description

        if minResponses > 0:
            self.minResponses = minResponses
        else:
            self.minResponses = -1

        if orderCandidatesBy == None:
            self.orderCandidatesBy = 'Acs'
        else:
            self.orderCandidatesBy = orderCandidatesBy

        if isOpenPoll == None:
            self.isOpenPoll = False
        else:
            self.isOpenPoll = isOpenPoll

        if openAt == None:
            self.openAt = datetime.utcnow()
        else:
            self.openAt = openAt

        if closeAt == None:
            self.closeAt = datetime.utcnow() + timedelta(days=7)
        else:
            self.closeAt = closeAt
        try:
            self.createdByUserId = User.userId
        except:
            print('Could not commit to database')
            return False
        self.createdAt = datetime.utcnow()
        self.isActive = 1

    def howManyCandidates(self):
        if self.Candidate == None:
            return 0
        else:
            return len(self.Candidate)

    def howManyResponses(self):
        if self.Response == None or self.Response == 0:
            return 0
        elif self.Candidate == None or self.Candidate == 0:
            print('There is no candidate saved yet')
            return 0
        else:
            return int(len(self.Response) / self.howManyCandidates())

    def getResponseDict(self):
        if self.Response == None or self.Response == 0:
            return []
        elif self.Candidate == None or self.Candidate == 0:
            print('There is no candidate saved yet')
            return []
        else:
            userId_list = []
            unique_userId_list = []
            for response in self.Response:
                userId_list.append(int(response.userId))
            for item in userId_list:
                if item not in unique_userId_list:
                    unique_userId_list.append(item)
            response_dict = {userId: [] for userId in unique_userId_list}
            activity_dict = {userId: bool for userId in unique_userId_list}
            for response in self.Response:
                if response.userId in response_dict:
                    response_dict[response.userId].append(response.candidateId)
                    if response.isActive != activity_dict[response.userId]:
                        activity_dict[response.userId] = response.isActive

            return [response_dict, activity_dict]


    def close(self):
        self.completedAt = datetime.utcnow()

    def isClosed(self):
        if self.completedAt:
            return True
        else:
            return False

    def validate(self):
        if self.title and self.orderCandidatesBy and self.createdByUserId and self.howManyCandidates() > 0:
            return True
        else:
            return False

    def get_id(self):
        return (self.pollId)

    def addCandidate(self, candidateDescription, displayOrder):
        if candidateDescription == None:
            print('You must enter the candidate details!')
            return False
        else:
            if self.orderCandidatesBy == 'SpecialOrder' and displayOrder == None:
                print('You must enter the order you want to display this candidate!')
                return False
            else:
                candidate = Poll.Candidate()
                candidate.candidateDescription = candidateDescription
                candidate.displayOrder = displayOrder
                # if self.get_id() != None:
                #     candidate.pollId=self.get_id()
                # else: 
                #      raise ValueError('Poll needs to be commited to DB before add candidate')
                candidate.isActive = True
                self.Candidate.append(candidate)

    def getCandidateId(self, key):
        for item in self.Candidate:
            if item.candidateDescription == key:
                return item.candidateId

    def addResponse(self, userId, preferenceXresponses):
        if self.isClosed():
            print('This poll has been closed since ', Poll.completedAt)
            return False
        else:
            if preferenceXresponses == None:
                print('You must enter preference order for each option')
                return False
            else:
                for key, value in preferenceXresponses.items():
                    response = Poll.Response()
                    response.userId = userId
                    response.pollId = self.pollId
                    response.candidateId = key
                    response.response = value
                    response.createdAt = datetime.utcnow()
                    response.isActive = True
                    # print("response check!")
                    self.Response.append(response)
                    try:
                        db.session.add(response)
                        db.session.commit()
                    except:
                        print('addResponse exception raised: ' + str(sys.exc_info()[0]))
                        return False
            return True

    def get_rawResult(self, jsonPayload=False):
        rawResult = {}
        tempdic = {}
        for candidate in self.Candidate:
            for i in range(self.howManyCandidates()):
                tempdic[i + 1] = tempdic.get(i + 1, 0)
            rawResult[candidate.candidateId] = rawResult.get(candidate.candidateId, tempdic)
            tempdic = {}
        for response in self.Response:
            if response.isActive:
                rawResult[response.candidateId][response.response] += 1

        if jsonPayload:
            # data={'rawResult':rawResult}
            # return make_response(jsonify(data))
            json.dumps(rawResult)
            return (rawResult)

        else:
            return rawResult

    def to_dict(self):
        noCandidates = self.howManyCandidates()
        noResponses = self.howManyResponses()
        canlist = self.Candidate
        # 'items': [item.to_dict() for item in resources.items],
        data = {
            'pollId': self.pollId,
            'title': self.title,
            'description': self.description,
            'createdAt': self.createdAt,
            'lastModifiedAt': self.lastModifiedAt,
            'completedAt': self.completedAt,
            'orderCandidatesBy': self.orderCandidatesBy,
            'minResponses': self.minResponses,
            'openAt': self.openAt,
            'closeAt': self.closeAt,
            'createdByUserId': self.createdByUserId,
            'isOpenPoll': self.isOpenPoll,
            'isActive': self.isActive,
            'noCandidates': noCandidates,
            'noResponses': noResponses,
            'candidates': [item.to_dict() for item in self.Candidate],
            'responses': [item.to_dict() for item in self.Response],
            'rawResult': self.get_rawResult(),
            'prefResult': self.get_prefResult()
        }
        return data

    def from_dict(self, data):
        for field in ['pollId', 'title', 'discription', 'lastModifiedAt', 'completedAt', 'orderCandidatesBy',
                      'minResponses', 'openAt', 'closeAt', 'createdByUserId', 'isOpenPoll', 'isActive']:
            if field in data:
                setattr(self, field, data[field])  ###############################################

    def get_prefResult(self, details=True):

        def getCanIndex(canList, key):
            listLen = len(canList)
            for index in range(listLen):
                if canList[index][1] == key:
                    return canList[index][0]

        def getCanList(self):
            CList = []
            howManyCandidates = self.howManyCandidates()
            howManyResponses = self.howManyResponses()

            for candidate in self.Candidate:
                temp = []
                temp.append(0)
                temp.append(candidate.candidateId)
                temp.append(candidate.candidateDescription)
                CList.append(temp)

            CList.sort()
            for index in range(len(CList)):
                CList[index][0] = index
            return CList

        def getResList(self):
            Result = {}
            RList = []
            howManyCandidates = self.howManyCandidates()
            howManyResponses = self.howManyResponses()
            for response in self.Response:
                if response.isActive:
                    if Result.get(response.userId) == None:
                        Result[response.userId] = []
                        for index in range(howManyCandidates):
                            Result[response.userId].append(0)
                        Result[response.userId][getCanIndex(getCanList(self), response.candidateId)] = response.response
                    else:
                        Result[response.userId][getCanIndex(getCanList(self), response.candidateId)] = response.response
            for key, value in Result.items():
                RList.append(value)
            return RList

        def findSN(list):
            temp = []
            if sum(list) != 0:
                if 0 in list:
                    for i in list:
                        if i != 0:
                            temp.append(i)
                    return min(temp)
                else:
                    return min(list)
            else:
                return -1

        def decision(count, totalCount, CList):
            global msg
            global currentResult

            result = (sorted(count, key=o.itemgetter(1), reverse=True))

            for i in range(len(result)):
                msg += str(result[i][1]) + "\t" + str(result[i][0]) + "\n"
                # print("++++++++++++++++",str(result[i][1])+"\t"+ str(result[i][0]) + "\n")
                # currentResult.append([result[i][1],result[i][0]])
                currentResult.append([result[i][1], result[i][0][1], result[i][0][2]])

            if (len(result) <= 1):
                return list(result[0]), True

            elif (totalCount == 0):
                return [], False
            else:
                if (result[0][1] / totalCount) <= 0.5:
                    return list(result[len(result) - 1]), False
                else:
                    return list(result[0]), True

        def prefResult(RList, CList, voteCount):
            global msg
            global currentResult

            responseCount = len(RList)
            candidateCount = len(CList)
            count = []
            totalCount = 0

            voteCount += 1

            currentResult.append(voteCount)
            for item in CList:
                count.append([item, 0])

            for index in range(responseCount):
                tempindex = RList[index].index(findSN(RList[index]))
                count[tempindex][1] += 1
                totalCount += 1

            results, decisionFlag = decision(count, totalCount, CList)

            if decisionFlag is False:
                if (results != []):
                    msg += "\nCandidate " + str(CList[count.index(results)][
                                                    2]) + " has the smallest number of votes and is eliminated from the count\n\n"
                    del (CList[count.index(results)])
                    for index in range(responseCount):
                        del (RList[index][count.index(results)])
                    prefResult(RList, CList, voteCount)
            else:
                msg += "\n" + str(count[0][1]) + "\t" + str(count[0][0]) + "\n"
                currentResult.append(voteCount + 1)
                currentResult.append([count[0][1], count[0][0][1], count[0][0][2]])
                msg += "\nCandidate " + str(results[0][2]) + " is elected\n"

        global msg
        msg = ""

        global currentResult
        currentResult = []

        CList = getCanList(self)
        RList = getResList(self)
        voteCount = 0
        prefResult(RList, CList, voteCount)
        if details:
            return currentResult
        else:
            return currentResult[len(currentResult) - 1]
