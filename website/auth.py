from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.senha, senha):
                flash('Logado com sucesso', category='sucesso')
                login_user(user, remember=True)
                return redirect(url_for('views.homepage'))
            else:
                flash('Senha Incorreta', category='erro')
        else:
            flash('Email não cadastrado', category='erro')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/inscreva-se', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')

        # User.query.delete()
        # db.session.commit()
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email já cadastrado', category='erro')
        elif len(email) < 4:
            flash('Email inválido', category='erro')
        elif len(nome) < 2:
            flash('Nome inválido', category='erro')
        elif senha1 != senha2:
            flash('As senhas não coincidem', category='erro')
        elif len(senha1) < 7:
            flash('A senhas precisa ter pelo menos 8 caracteres', category='erro')
        else:
            new_user = User(email=email, senha=generate_password_hash(senha1, method='sha256'),
                            nome=nome, sobrenome=sobrenome)
            db.session.add(new_user)
            db.session.commit()
            flash('Conta criada', category='sucesso')
            login_user(new_user, remember=True)
            return redirect(url_for('views.homepage'))

    return render_template('inscreva_se.html', user=current_user)
