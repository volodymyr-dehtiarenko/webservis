import os
from flask_sqlalchemy import SQLAlchemy
from web import app

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'hardsecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:12345@localhost/web"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)