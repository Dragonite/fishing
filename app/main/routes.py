from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
# from guess_language import guess_language
from app import db


from app.models import User, Poll
from app.main import bp

from app.pollForm import CreatePollForm

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])

def index():
    return render_template('index.html', title='Home')




@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = CreatePollForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('create.html', title='Create a Poll', form=form)


@bp.route('/help')
def help():
    return render_template("help.html", title='Help')


@bp.route('/current')
def current():
    return render_template("current.html", title='Current Polls')


@bp.route('/completed')
def completed():
    return render_template("completed.html", title='Completed Polls')


# @bp.route('/create')
# # @login_required
# def create():
#     return render_template("create.html", title='Create A Poll')

@bp.route('/users')
# @login_required
def users():
    return render_template("users.html", title='Users')

# @bp.route('/userUpdate', methods=['GET', 'POST'])
# # @login_required
# def userUpdate():
#     if current_user.is_authenticated:
#         user = User.query().filter(User.name==form.username.data)
#         data = user.data
#         data["filedname"] =data
#         user.data = data
#         flag_modified(user, "data")
#         db.session.merge(user)
#         db.session.flush()
#         db.session.commit() 
#         return render_template("users.html", title='Users')

@bp.route('/profile')
# @login_required
def profile():
    return render_template("profile.html", title='My Profile')


