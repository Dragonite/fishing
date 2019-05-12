import os
from dotenv import load_dotenv


# basedir=os.path.abspath(os.path.dirname(__file__))
DATABASE_URL=''
dbName='app.db'


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    '''SQLALCHEMY_DATABASE = os.environ.get(DATABASE_URL) or 'sqlite:///' + os.path.join(basedir, dbName)'''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db' )
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

class testingConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


