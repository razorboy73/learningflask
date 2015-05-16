__author__ = 'workhorse'
import os
from config import basedir, ADMINS
from flask import Flask

from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

lm.login_view='login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

mail = Mail(app)

from app import views, models

from .momentjs import momentjs
app.jinja_env.globals['momentjs'] = momentjs



if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')