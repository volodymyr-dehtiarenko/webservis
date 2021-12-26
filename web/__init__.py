from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from admin.admin import admin
from customer_profile.customer_profile import customer_profile



app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object('config')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(customer_profile, url_prefix='/customer_profile')

db = SQLAlchemy(app)


from web import views
from web import models
