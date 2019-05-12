from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
# from guess_language import guess_language
from app import db


from app.models import User, Poll
from app.controllers import createPoll, getCurrentPoll, getClosedPoll, getAllUsers, getPollById,getResults
from app.main import bp

from app.pollForm import CreatePollForm
from app.registrationForm import RegistrationForm

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])

def index():
    return render_template('index.html', title='Home')




@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = CreatePollForm()
    if form.validate_on_submit():
        poll=Poll(title=form.title.data, description=form.description.data,  minResponses=0, orderCandidatesBy=None, isOpenPoll=form.isOpen.data, openAt=None, closeAt=None, User=current_user)
        candidates=form.options
        for item in candidates:
            # print(item.data)
            poll.addCandidate(item.data, None)

        if createPoll(poll):
            flash('Poll has been created successfully!')
            return redirect(url_for('main.index'))
        else:
            flash('something is wrong!')
            return redirect(url_for('main.create'))
    return render_template('create.html', title='Create a Poll', form=form)


@bp.route('/help')
def help():
    return render_template("help.html", title='Help')


@bp.route('/current')
def current():
    poll=getCurrentPoll()
    return render_template("current.html", title='Current Polls', poll=poll)


@bp.route('/completed')
def completed():
    poll=getClosedPoll()
    return render_template("completed.html", title='Completed Polls', poll=poll)


@bp.route('/users')
# @login_required
def users():
    user=getAllUsers()
    return render_template("users.html", title='Users', user=user)


@bp.route('/profile')
# @login_required
def profile():
    return render_template("profile.html", title='My Profile')



@bp.route('/test', methods=['GET', 'POST'])
def test():
    poll=getPollById(1)
    getResults(poll)
    return render_template("test.html", title='test', poll=poll)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username=form.username.data
        user.email=form.email.data
        user.firstName=form.firstName.data
        user.lastName=form.lastName.data
        user.ad_street=form.ad_street.data
        user.ad_suburb=form.ad_suburb.data
        user.ad_state=form.ad_state.data
        user.ad_country=form.ad_country.data
        if createUser(user,form.password.data):
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)
