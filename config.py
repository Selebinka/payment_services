import os
from environs import Env


basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()

SHOP_ID = env.str("SHOP_ID")
SECRET_KEY = env.str("SECRET_KEY")
PAYWAY = env.str("PAYWAY")

WHOOSH_ENABLED = os.environ.get('HEROKU') is None

class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'payments.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = True

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')