import unittest, os
from app import app, db
from app.models import User, Poll
from app.controllers import *
from assertpy import assert_that

class pollModelCase(unittest.TestCase):
    
    def setUp(self):
        basedir=os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app=app.test_client()
        db.create_all()

        
        title='where is your favorite fishing spot?'
        description='survey to find out the most favorite fishing spot in Perth'
        user=User.query.filter_by(username='luna').first()
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
        for i in range(6):
            db.session.add(poll.candidate[i])
        db.session.commit()
# assert_that(theBiscuit, is_(equal_to(myBiscuit)))


    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__=='__main__':
    unittest.main()

    