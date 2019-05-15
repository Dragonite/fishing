from datetime import datetime, timedelta
from app import create_app, db
from config import Config
import unittest, os
from unittest import TestSuite, TestCase
from app.models import User, Poll
from app.controllers import *
from assertpy import assert_that
import os


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None



class userControllerCase(unittest.TestCase):
    
    def setUp(self):
        # basedir=os.path.abspath(os.path.dirname(__file__))
        # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        # self.app=app.test_client()
        self.app=create_app(TestConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()
    
        luna=User()
        luna.username='luna'
        luna.firstName='Luna'
        luna.lastName='Lee'
        luna.email='22sfdsdf187554@student.edu.au'
        luna.isAdmin=True
        
        haolin=User()
        haolin.username='haolin'
        haolin.firstName='Haolin'
        haolin.lastName='Wu'
        haolin.email='abc21706sdsfdf137@student.edu.au'
        haolin.isAdmin=True

        db.session.add(luna)
        db.session.add(haolin)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        # os.remove("test.db")

    def test_createUser(self):
        validUser=User()
        validUser.username='creatusertest'
        validUser.firstName='creatusertest'
        validUser.lastName='Lee'
        validUser.email='a221875dfs54@student.edu.au'
        validUser.isAdmin=True
        valid_pwd='1234'
        invalid_pwd=''
       
        assert_that(createUser(validUser, valid_pwd)).is_equal_to(True)
        assert_that(type(User.query.filter_by(username=validUser.username).first().userId)).is_equal_to(type(1))
        
        assert_that(createUser(validUser, invalid_pwd)).raises
            
        emptyUser=User()
        assert_that(createUser(emptyUser, valid_pwd)).raises
        assert_that(createUser(emptyUser, invalid_pwd)).raises

    def test_modifyUser(self):
        User.query.first()

    def test_archiveUser(self):
        User.query.first()

    def test_getUserById(self):
        userId=1
        assert_that(getUserById(userId).userId).is_equal_to(userId)
    
    def test_getUserByUsername(self): 
        username='abcwerhasdfolin'
        assert_that(getUserByUsername(username).username).is_equal_to(username)

    def test_login_time(self):
        

class userModelCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(TestConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_user_init(self):
        user=User()
        assert_that(type(user.createdAt)).is_equal_to(type(datetime.utcnow()))
        assert_that(user.lastModifiedAt).is_equal_to(None)
        assert_that(user.isActive).is_equal_to(True)
        assert_that(user.isAdmin).is_equal_to(False)
    def test_user_validate(self):
        validUser=User()
        invalidUser=User()
        validUser.firstName='firstname'
        validUser.username='username'
        validUser.email='emailaddress@email.com'
        assert_that(validUser.validate()).is_equal_to(True)
        assert_that(invalidUser.validate()).is_equal_to(False)

        invalidUser.firstName='firstname'
        invalidUser.username='username'
        invalidUser.email=None
        assert_that(invalidUser.validate()).is_equal_to(False)

        invalidUser.firstName=None
        invalidUser.username='username'
        invalidUser.email='emailaddress@email.com'
        assert_that(invalidUser.validate()).is_equal_to(False)
 

        invalidUser.firstName='firstname'
        invalidUser.username='username'
        invalidUser.email=None
        

        assert_that(invalidUser.validate()).is_equal_to(False)

    def test_user_set_password(self):
        luna=User()
        luna.username='abclsdwrfuna'
        luna.firstName='Luna'
        luna.lastName='Lee'
        luna.email='abc2218sdfsdf7554@student.edu.au'
        luna.isAdmin=True
        luna.set_password('1234')
        assert_that(type(luna.pwdHash)).is_equal_to(type('abc'))

    def test_user_check_password(self):
        luna=User()
        luna.username='abclsdwrfuna'
        luna.firstName='Luna'
        luna.lastName='Lee'
        luna.email='abc2218sdfsdf7554@student.edu.au'
        luna.set_password('1234')
        assert_that(luna.check_password('1234')).is_equal_to(True)

    def test_user_get_id(self):
        luna=User()
        luna.username='username'
        luna.firstName='Luna'
        luna.lastName='Lee'
        luna.email='lunauser@student.edu.au'
        luna.isAdmin=True
        db.session.add(luna)
        db.session.commit()
        assert_that(type(luna.get_id())).is_equal_to(type(1))


class pollModelCase(unittest.TestCase):
    
    def setUp(self):
        # basedir=os.path.abspath(os.path.dirname(__file__))
        # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        # self.app=app.test_client()
        self.app=create_app(TestConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()
        luna=User()
        luna.username='luna'
        luna.firstName='Luna'
        luna.lastName='Lee'
        luna.email='abc2218sdfsdf7554@student.edu.au'
        luna.isAdmin=True
        
        haolin=User()
        haolin.username='abcwerhasdfolin'
        haolin.firstName='abcHaolin'
        haolin.lastName='Wu'
        haolin.email='abc21706sdsfdf137@student.edu.au'
        haolin.isAdmin=True


        db.session.add(luna)
        db.session.add(haolin)
        db.session.commit()


        title='where is your favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(username='luna').first()
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidateBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidateBy, isOpenPoll, openAt, closeAt, user)

        db.session.add(poll)
        db.session.commit()

        candidate1 = Poll.Candidate()
        candidate1.candidateDescription='Narrows Bridge Perth'
        candidate1.displayOrder=None
        candidate1.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate1.isActive=True


        candidate2 = Poll.Candidate()
        candidate2.candidateDescription='White Hills Mandurah'
        candidate2.displayOrder=None
        candidate2.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate2.isActive=True


        candidate3 = Poll.Candidate()
        candidate3.candidateDescription='North Mole Fremantle'
        candidate3.displayOrder=None
        candidate3.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate3.isActive=True


        candidate4 = Poll.Candidate()
        candidate4.candidateDescription='Floreat Drain Floreat'
        candidate4.displayOrder=None
        candidate4.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate4.isActive=True



        candidate5 = Poll.Candidate()
        candidate5.candidateDescription='Ricey Beach And Radar Reef Rottnest Island'
        candidate5.displayOrder=None
        candidate5.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate5.isActive=True


        candidate6 = Poll.Candidate()
        candidate6.candidateDescription='Lancelin Jetty Lancelin'
        candidate6.displayOrder=None
        candidate6.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate6.isActive=True


     
        db.session.add(candidate1)
        db.session.commit()
        db.session.add(candidate2)
        db.session.commit()
        db.session.add(candidate3)
        db.session.commit()
        db.session.add(candidate4)
        db.session.commit()
        db.session.add(candidate5)
        db.session.commit()
        db.session.add(candidate6)
        db.session.commit()




        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_poll_init(self):
        
        
        title='test_poll_init - where is your favorite fishing spot?'
        description='test_poll_init - survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(userId=1).first()
 
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidatesBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, user)
        
        assert_that(len(poll.Candidate)).is_equal_to(0)
        assert_that(len(poll.Response)).is_equal_to(0)


        assert_that(type(poll.createdAt)).is_equal_to(type(datetime.utcnow())) ##needs review
        assert_that(poll.title).is_equal_to(title)
        assert_that(poll.description).is_equal_to(description)
        assert_that(poll.createdByUserId).is_equal_to(user.userId)
        assert_that(poll.minResponses).is_equal_to(minResponses)
        assert_that(poll.orderCandidatesBy).is_equal_to('Acs')
        assert_that(poll.isOpenPoll).is_equal_to(False)



        assert_that(poll.openAt.strftime("%x")).is_equal_to(datetime.utcnow().strftime("%x"))
        assert_that(poll.closeAt.strftime("%x")).is_equal_to((datetime.utcnow()+timedelta(days=7)).strftime("%x"))   #need to check +7days
        assert_that(poll.lastModifiedAt).is_equal_to(None)
        assert_that(poll.completedAt).is_equal_to(None)
        
        assert_that(poll.isActive).is_equal_to(1)


    def test_poll_howManyCandidates(self):
        title='test_poll_howManyCandidates- where is your favorite fishing spot?'
        description='test_poll_howManyCandidates- survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(userId=1).first()
 
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidatesBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, user)

        assert_that(poll.howManyCandidates()).is_equal_to(0)

        poll.addCandidate('test_poll_howManyCandidates- Narrows Bridge Perth',None)
        poll.addCandidate('test_poll_howManyCandidates- White Hills Mandurah',None)
        poll.addCandidate('test_poll_howManyCandidates- North Mole Fremantle',None)
        poll.addCandidate('test_poll_howManyCandidates- Floreat Drain Floreat',None)
        poll.addCandidate('test_poll_howManyCandidates- Ricey Beach And Radar Reef Rottnest Island',None)
        poll.addCandidate('test_poll_howManyCandidates- Lancelin Jetty Lancelin',None)

        assert_that(poll.howManyCandidates()).is_equal_to(6)

    def test_poll_howManyResponses(self):

        poll=Poll.query.filter_by(pollId=1).first()
        
        assert_that(poll.howManyResponses()).is_equal_to(0)

        response1=Poll.Response()
        response1.userId=userId
        response1.pollId=poll.pollId
        response1.candidateId=1
        response1.response=1
        response1.createdAt=datetime.utcnow()
        response1.isActive=True
        poll.Response.append(response1)

        ## needs more work




    def test_poll_close(self):
        title='where is your favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(userId=1).first()
 
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidatesBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, user)
        
        poll.close()

        assert_that(poll.completedAt.strftime("%x")).is_equal_to(datetime.utcnow().strftime("%x"))

    
    def test_poll_isClosed(self):
        title='where is your favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(userId=1).first()
 
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidatesBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, user)
        
        assert_that(poll.isClosed()).is_equal_to(False)
        
        poll.close()

        assert_that(poll.isClosed()).is_equal_to(True)



    
    def test_poll_addResponse(self):
        poll=Poll.query.filter_by(pollId=1).first()
            ## needs more work





class pollControllerCase(unittest.TestCase):
    
    def setUp(self):

        # basedir=os.path.abspath(os.path.dirname(__file__))
        # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        # self.app=app.test_client()
        # db.create_all()
        self.app=create_app(TestConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()
        luna=User()
        luna.username='luna'
        luna.firstName='Luna'
        luna.lastName='Lee'
        luna.email='abc2218sdfsdf7554@student.edu.au'
        luna.isAdmin=True
        
        haolin=User()
        haolin.username='abcwerhasdfolin'
        haolin.firstName='abcHaolin'
        haolin.lastName='Wu'
        haolin.email='abc21706sdsfdf137@student.edu.au'
        haolin.isAdmin=True


        db.session.add(luna)
        db.session.add(haolin)
        db.session.commit()

        title='where is your favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(username='luna').first()
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidateBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidateBy, isOpenPoll, openAt, closeAt, user)

        db.session.add(poll)
        db.session.commit()

        candidate1 = Poll.Candidate()
        candidate1.candidateDescription='Narrows Bridge Perth'
        candidate1.displayOrder=None
        candidate1.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate1.isActive=True


        candidate2 = Poll.Candidate()
        candidate2.candidateDescription='White Hills Mandurah'
        candidate2.displayOrder=None
        candidate2.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate2.isActive=True


        candidate3 = Poll.Candidate()
        candidate3.candidateDescription='North Mole Fremantle'
        candidate3.displayOrder=None
        candidate3.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate3.isActive=True


        candidate4 = Poll.Candidate()
        candidate4.candidateDescription='Floreat Drain Floreat'
        candidate4.displayOrder=None
        candidate4.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate4.isActive=True



        candidate5 = Poll.Candidate()
        candidate5.candidateDescription='Ricey Beach And Radar Reef Rottnest Island'
        candidate5.displayOrder=None
        candidate5.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate5.isActive=True


        candidate6 = Poll.Candidate()
        candidate6.candidateDescription='Lancelin Jetty Lancelin'
        candidate6.displayOrder=None
        candidate6.pollId=Poll.query.filter_by(pollId=1).first().pollId
        candidate6.isActive=True


     
        db.session.add(candidate1)
        db.session.commit()
        db.session.add(candidate2)
        db.session.commit()
        db.session.add(candidate3)
        db.session.commit()
        db.session.add(candidate4)
        db.session.commit()
        db.session.add(candidate5)
        db.session.commit()
        db.session.add(candidate6)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_createPoll(self):
        title='test_createPoll- where is your third favorite fishing spot?'
        description='test_createPoll- survey to find out the most favorite fishing spot in Perth'
        user=User()
        user.userId=1
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidateBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidateBy, isOpenPoll, openAt, closeAt, user)
        poll.addCandidate('test_createPoll- Narrows Bridge Perth',None)
        poll.addCandidate('test_createPoll- White Hills Mandurah',None)
        poll.addCandidate('test_createPoll- North Mole Fremantle',None)
        poll.addCandidate('test_createPoll- Floreat Drain Floreat',None)
        poll.addCandidate('test_createPoll- Ricey Beach And Radar Reef Rottnest Island',None)
        poll.addCandidate('test_createPoll- Lancelin Jetty Lancelin',None)

        assert_that(createPoll(poll)).is_equal_to(True)

    def test_modifyPoll(self):
        poll=Poll.query.filter_by(pollId=1).first()

        assert_that(poll.lastModifiedAt).is_equal_to(None)

        poll.minResponses=6
        
        assert_that(modifyPoll(poll)).is_equal_to(True)
        assert_that(poll.lastModifiedAt.strftime("%x")).is_equal_to(datetime.utcnow().strftime("%x"))

    def test_archivePoll(self):

        poll=Poll.query.filter_by(pollId=1).first()

        assert_that(archivePoll(poll)).raises

        poll.close()

        assert_that(archivePoll(poll)).is_equal_to(True)


    def test_getPollById(self):
        
        poll=Poll.query.filter_by(pollId=1).first()

        assert_that(getPollById(1)).is_equal_to(poll)
      


def suite():
    
    suite = unittest.TestSuite()
    suite.addTest(userModelCase('test_user_init'))
    suite.addTest(userModelCase('test_user_validate'))
    suite.addTest(userModelCase('test_user_set_password'))
    suite.addTest(userModelCase('test_user_check_password'))
    suite.addTest(userModelCase('test_user_get_id'))
    suite.addTest(userControllerCase('test_createUser'))
    suite.addTest(userControllerCase('test_modifyUser'))
    suite.addTest(userControllerCase('test_archiveUser'))
    suite.addTest(userControllerCase('test_getUserById'))
    suite.addTest(userControllerCase('test_getUserByUsername'))
    suite.addTest(pollModelCase('test_poll_init'))
    suite.addTest(pollControllerCase('test_createPoll'))
    return suite

        



if __name__=='__main__':
    unittest.main(verbosity=2)


