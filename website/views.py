from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def homepage():
    return render_template('home.html')


@views.route('/criadores')
def criadores():
    return render_template('about.html')
