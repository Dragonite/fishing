import unittest, os
from unittest import TestSuite, TestCase
from app import app, db
from app.models import User, Poll
from app.controllers import *
from assertpy import assert_that
import os

class userControllerCase(unittest.TestCase):
    
    def setUp(self):
        basedir=os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app=app.test_client()
        db.create_all()
    
        luna=User()
        luna.username='abclsdwrfuna'
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
        # os.remove("test.db")

    def test_createUser(self):
        validUser=User()
        validUser.username='a123dsddsfdsd2424aaaaaluna'
        validUser.firstName='a24aaaaLuna'
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



class userModelCase(unittest.TestCase):
    def setUp(self):
        basedir=os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app=app.test_client()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
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

    # def test_user_repr(self):
    #     luna=User()
    #     luna.username='abclsdwrfuna'
    #     luna.firstName='Luna'
    #     luna.lastName='Lee'
    #     luna.email='abc2218sdfsdf7554@student.edu.au'
    #     luna.isAdmin=True

    #     assert_that(luna.repr()).is_equal_to('<User {abclsdwrfuna}>')

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
    return suite



if __name__=='__main__':
    unittest.main()