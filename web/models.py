from web import db
from datetime import datetime


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    address = db.Column(db.String(150))
    tel_number = db.Column(db.Integer(), unique=True, nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=True)
    psw = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<user {self.id, self.email}>"


# class Super_user(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(50), unique=True, nullable=True)
#     psw = db.Column(db.String(500), nullable=True)
#
#     def __repr__(self):
#         return f"<user {self.id, self.email}>"
