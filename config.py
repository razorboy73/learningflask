__author__ = 'workhorse'
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = "KrisKrosMakeYouWannaJumpJump"

OPENID_PROVIDERS = [
     {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,"app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")


# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = ('joshadamkerbel@gmail.com')
MAIL_PASSWORD = ('Swingline12345@@')

# administrator list
ADMINS = ['joshadamkerbel@gmail.com', 'josh@rallyyourgoals.com']

#pagination
POSTS_PER_PAGE = 3

#profiling
SQLALCHEMY_RECORD_QUERIES = True
# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5
