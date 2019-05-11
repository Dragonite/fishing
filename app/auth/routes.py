from flask import render_template, redirect, url_for, flash, Markup
from flask_login import login_user, logout_user, current_user

from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm  # ,  ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
import datetime

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # if user is None or not user.check_password(form.password.data):
        #     flash('Invalid username or password')
        #     return redirect(url_for('login'))
        # login_user(user, remember=form.remember_me.data)
        # next_page = request.args.get('next')   #########
        # if not next_page or url_parse(next_page).netloc != '':
        #      next_page = url_for('index')
        # return redirect(url_for('next_page'))

        if user is None or not user.check_password(form.password.data):
            flash(Markup('<script>Notify("Invalid username or password.", null, null, "danger")</script>'))
            return redirect(url_for('login'))
            # session['was_once_logged_in'] = True
        login_user(user, remember=form.remember_me.data)
        flash(Markup('<script>Notify("You have successfully logged in.", null, null, "success")</script>'))
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash(Markup('<script>Notify("You have successfully logged yourself out.", null, null, "success")</script>'))
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, firstName=form.firstName.data,
                    lastName=form.lastName.data, ad_street=form.ad_street.data, ad_suburb=form.ad_suburb.data,
                    ad_state=form.ad_state.data, createdAt=datetime.utcnow(), isActive=1, isAdmin=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)
