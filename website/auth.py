from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/inscreva-se')
def sign_up():
    return render_template('inscreva_se.html')
