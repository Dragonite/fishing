from flask import render_template, redirect, url_for, flash, Markup
from flask_login import login_user, logout_user, current_user

from app import db
from app.auth import bp
from app.auth.forms import LoginForm#, RegistrationForm  ,  ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from app.controllers import login_time

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(Markup('<script>Notify("Invalid username or password.", null, null, "danger")</script>'))
            return redirect(url_for('auth.login'))
            # session['was_once_logged_in'] = True
        login_user(user, remember=form.remember_me.data)
        flash(Markup('<script>Notify("You have successfully logged in.", null, null, "success")</script>'))
        login_time(user)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash(Markup('<script>Notify("You have successfully logged yourself out.", null, null, "success")</script>'))
    return redirect(url_for('main.index'))

