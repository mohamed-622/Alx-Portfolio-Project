from . import db
from .models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
import re


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')

        user = User.query.filter_by(phone_number=phone_number).first()
        if user:
            if (user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('No account with this number.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'], strict_slashes=False)
def sign_up():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        name = request.form.get('Name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(phone_number=phone_number).first()
        phone_number_pattern = re.compile(r'^0\d{9}$')

        if user:
            flash('Account with this number already exists.', category='error')
        elif not phone_number_pattern.match(phone_number):
            flash('Phone number format: 0xxxxxxxxx', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(phone_number=phone_number, name=name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
