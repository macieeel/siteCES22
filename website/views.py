from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def homepage():
    return render_template('home.html', user=current_user)


@views.route('/criadores')
def criadores():
    return render_template('about.html', user=current_user)
