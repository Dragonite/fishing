from flask import render_template, flash, redirect, url_for, Markup
from flask_login import login_required, current_user, login_user, logout_user

from app import app, db
from app.forms import LoginForm, CreatePollForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CreatePollForm()
    if form.validate_on_submit():
        # message = Markup(
        #     # '<script>Notify("Login requested for user {}, Remember me = {}", null, null, "danger")</script>'.format(
        #     #     form.username.data, form.remember_me.data))
        # flash(message)
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('create.html', title='Create a Poll', form=form)


@app.route('/help')
def help():
    return render_template("help.html", title='Help')


@app.route('/current')
def current():
    return render_template("current.html", title='Current Polls')


@app.route('/completed')
def completed():
    return render_template("completed.html", title='Completed Polls')


# @app.route('/create')
# # @login_required
# def create():
#     return render_template("create.html", title='Create A Poll')

@app.route('/users')
# @login_required
def users():
    return render_template("users.html", title='Users')


@app.route('/profile')
# @login_required
def profile():
    return render_template("profile.html", title='My Profile')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(Markup('<script>Notify("You have successfully logged yourself out.", null, null, "success")</script>'))
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
