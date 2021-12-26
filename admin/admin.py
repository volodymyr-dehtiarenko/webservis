from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
engine = create_engine('mysql+pymysql://admin:12345@localhost/24servis')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
metadata = MetaData(bind=engine)
customers = Table('customers', metadata, autoload=True)


def isLogged():
    return True if session.get('admin_logged') else False


def login_admin():
    session['admin_logged'] = 1


def logout_admin():
    session.pop('admin_logged', None)
    db = None


@admin.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    pass


@admin.teardown_request
def teardown_request(request):
    db_session.remove()


# Main page Blueprint Admin
@admin.route('/')
def index():
    if not isLogged():
        return redirect(url_for('.login'))
    return render_template('admin/admin_panel.html', title='Dashboard')


# LoginAdmin
@admin.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form['admin_login'] and request.form['admin_pwd']:
            name = request.form['admin_login']
            login_admin()
            return render_template('admin/admin_panel.html', name=name)
        else:
            flash('Error login/password')
    return render_template('admin/admin_login.html', title='Admin panel')


# Logout Admin
@admin.route('/logout', methods=["POST", "GET"])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))

    logout_admin()

    return redirect(url_for('.login'))


# Customers List Information
@admin.route('/customers_list')
def customers_list():
    if not isLogged():
        return redirect(url_for('.login'))
    cl = []
    if engine:
        flash("Conection with DB is OK! ", category='message')
        try:
            con = engine.connect()
            cl = con.execute('SELECT id, date, name, surname, address, tel_number, email FROM customers')
        except:
            flash("Conection with DB error! ", category='error')
    return render_template('admin/admin_customers_list.html', title='Customers', cl=cl)
