from web import app
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash
from datetime import datetime


from flask import render_template, request, redirect
from .models import Customers, db



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/price')
def price():
    return render_template('price.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=["POST", "GET"])
def main_login():

        return render_template('customer_profile/customer_panel.html')



@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        psw_form = request.form['psw']
        cust = Customers(
            date=datetime.today(),
            name=request.form['name'],
            surname=request.form['surname'],
            address=request.form['address'],
            tel_number=request.form['tel_number'],
            email=request.form['email'],
            psw=generate_password_hash(psw_form))
        # add to database
        db.session.add(cust)
        db.session.commit()
        return render_template('main_login.html')
    else:
        print("Sorry Error")
        return render_template('register.html')






