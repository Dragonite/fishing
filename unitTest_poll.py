import unittest, os
from app import app, db
from app.models import User, Poll
from app.controllers import *
from assertpy import assert_that
from datetime import datetime
from datetime import timedelta  


class pollModelCase(unittest.TestCase):
    
    def setUp(self):
        basedir=os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app=app.test_client()
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

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_poll_init(self):
        
        
        title='where is your favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(userId=1).first()
 
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidatesBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidatesBy, isOpenPoll, openAt, closeAt, user)
        
        assert_that(type(poll.createdAt)).is_equal_to(type(datetime.utcnow()))
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

        
        poll.addCandidate('Narrows Bridge Perth',None)
        poll.addCandidate('White Hills Mandurah',None)
        poll.addCandidate('North Mole Fremantle',None)
        poll.addCandidate('Floreat Drain Floreat',None)
        poll.addCandidate('Ricey Beach And Radar Reef Rottnest Island',None)
        poll.addCandidate('Lancelin Jetty Lancelin',None)

       
        db.session.add(poll)
        # for i in range(6):
        #     db.session.add(poll.candidate[i])
        db.session.commit()




class pollControllerCase(unittest.TestCase):
    
    def setUp(self):
        basedir=os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app=app.test_client()
        db.create_all()

        
        title='where is your second favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User()
        user.userId=1
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidateBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidateBy, isOpenPoll, openAt, closeAt, user)
        poll.addCandidate('Narrows Bridge Perth',None)
        poll.addCandidate('White Hills Mandurah',None)
        poll.addCandidate('North Mole Fremantle',None)
        poll.addCandidate('Floreat Drain Floreat',None)
        poll.addCandidate('Ricey Beach And Radar Reef Rottnest Island',None)
        poll.addCandidate('Lancelin Jetty Lancelin',None)

        db.session.add(poll)
        # for i in range(6):
        #     db.session.add(poll.candidate[i])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_createPoll(self):
        title='where is your third favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User()
        user.userId=1
        minResponses=5 #if not specified, the default value is -1 which will be ignored
        orderCandidateBy=None #if not specified, the default value is alphabel acending 'Acs'
        isOpenPoll=None #if not specified, the default value is False
        openAt=None #if not specified, the default value is utcnow()
        closeAt=None  # if not specified, the default value is today + 7 days
        poll=Poll(title, description, minResponses, orderCandidateBy, isOpenPoll, openAt, closeAt, user)
        poll.addCandidate('Narrows Bridge Perth',None)
        poll.addCandidate('White Hills Mandurah',None)
        poll.addCandidate('North Mole Fremantle',None)
        poll.addCandidate('Floreat Drain Floreat',None)
        poll.addCandidate('Ricey Beach And Radar Reef Rottnest Island',None)
        poll.addCandidate('Lancelin Jetty Lancelin',None)

        assert_that(createPoll(poll)).is_equal_to(True)


def suite():
    
    suite = unittest.TestSuite()
    suite.addTest(pollModelCase('test_poll_init'))
    suite.addTest(pollControllerCase('test_createPoll'))
    return suite



if __name__=='__main__':
    unittest.main()
    