from flask import Blueprint, render_template, session, redirect, url_for



customer_profile = Blueprint('customer_profile', __name__, template_folder='templates', static_folder='static')


# Main page
@customer_profile.route('/')
def index():
    name = 'Ivan'
    return render_template('customer_profile/customer_panel.html', title = 'Панель клиента', name = name)

# Customer new order
@customer_profile.route('/order')
def customer_new_order():
    return render_template('customer_profile/customer_order.html', title = 'Новый заказ')


# Logout Customer
@customer_profile.route('/logout')
def logout():
    return render_template('.index')