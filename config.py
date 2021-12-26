import os


_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True


ADMINS = frozenset(['volodymyr.dehtiarenko@gmail.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:12345@localhost/24servis"
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"