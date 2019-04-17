import os
basedir=os.path.abspath(os.path.dirname(__file__))
DATABASE_URL=''
dbName='test.db'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    '''SQLALCHEMY_DATABASE = os.environ.get(DATABASE_URL) or 'sqlite:///' + os.path.join(basedir, dbName)'''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, dbName)
    SQLALCHEMY_TRACK_MODIFICATIONS  = False