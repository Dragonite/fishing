from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app, Markup
from flask_login import current_user, login_required
# from flask_babel import _, get_locale
# from guess_language import guess_language
from app import db
import json

from app.models import User, Poll
from app.controllers import createUser, createPoll, getCurrentPolls, getClosedPolls, getAllUsers, getPollById, getUserById
from app.main import bp

from app.pollForm import CreatePollForm,makeResponseForm
from app.registrationForm import RegistrationForm




@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])

def index():
    return render_template('index.html', title='Home')




@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreatePollForm()
    if form.validate_on_submit():
        validationPoll=Poll.query.filter_by(title=form.title.data).first()
        if validationPoll!= None:

            flash('There is alreay a poll created with the same title.')
            return redirect(url_for('main.create'))

        else:
            poll=Poll(title=form.title.data, description=form.description.data,  minResponses=0, orderCandidatesBy=None, isOpenPoll=form.isOpen.data, openAt=None, closeAt=None, User=current_user)
            candidates=form.options
            nullCount=len(form.options)

            for item in candidates:
                if item.data != None and item.data != "":
                    poll.addCandidate(item.data, None)
                    nullCount-=1
            if nullCount > (len(form.options)-2):
                flash('There is not enough choice to make this poll.')
                return redirect(url_for('main.create'))
            else:  
                if createPoll(poll)==True:
                    flash('Poll has been created successfully!')
                    return render_template("currentPollView.html", title=poll.title, poll=poll, form=form)

                else:
                    flash('something is wrong!')
                    return redirect(url_for('main.create'))
    return render_template('create.html', title='Create a Poll', form=form)


@bp.route('/help')
def help():
    return render_template("help.html", title='Help')


@bp.route('/current', methods=['GET', 'POST'])
def current():
    polls=getCurrentPolls()
    users=getAllUsers()
    if current_user.is_authenticated:
        if current_user.isAdmin:
            polls=getCurrentPolls(isAdmin=True)
            users=getAllUsers()
            return render_template("current.html", title='Current Polls', polls=polls, users=users)
    return render_template("current.html", title='Current Polls', polls=polls, users=users)







@bp.route('/current/<int:pollId>', methods=['GET', 'POST'])
def current_view(pollId):
    users = getAllUsers()
    poll=getPollById(pollId)
    if poll:
        responseParameter=[]
        for item in poll.Candidate:
            responseParameter.append((item.candidateId, item.candidateDescription))
        form=makeResponseForm(responseParameter)
        
        if form.validate_on_submit():
            pass
                ##do not delete
                # response=form.response
                # res={}
                # if Poll.Response.query.filter_by(userId=current_user.userId).all() != None:
                #     flash('you have voted for this poll already.')
                # else:
                #     if poll.addResponse(current_user.userId, res):
                #         flash('you have successfully voted for this poll')
                #         return redirect(url_for('main.current'))
                #     else:
                #         flash('Something went wrong')
        renderedtitle=poll.title
        return render_template("currentPollView.html", title=renderedtitle, poll=poll, form=form, users=users)

    else:
        flash('Poll does not exist')    
    return redirect(url_for('main.current'))

@bp.route('/completed', methods=['GET', 'POST'])
def completed():
    polls=getClosedPolls(isAdmin=False)
    users = getAllUsers()
    if current_user.is_authenticated:
        if current_user.isAdmin:
            polls=getClosedPolls(isAdmin=True)
            users = getAllUsers()
            return render_template("completed.html", title='Completed Polls', polls=polls, users=users)
    return render_template("completed.html", title='Completed Polls', polls=polls, users=users)
@bp.route('/completed/<int:pollId>', methods=['GET', 'POST'])
def completed_view(pollId):
    poll=getPollById(pollId)
    users = getAllUsers()
    if poll:
        renderedtitle=poll.title
    else:
        renderedtitle="Oops, something is wrong"
    return render_template("completedPollView.html", title=renderedtitle, poll=poll, users=users)



@bp.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    if current_user.isAdmin:
        users=getAllUsers()
        return render_template("users.html", title='Users', users=users)
    else:
        flash(Markup('<script>Notify("Only an admin user can view this page!", null, null, "danger")</script>'))
        return redirect(url_for('main.index'))

@bp.route('/users/delete/<int:userId>', methods=['GET', 'POST'])
@login_required
def delete_user(userId):
    pass
    return render_template("users.html", title='Users', users=users)

@bp.route('/polls/delete/<int:pollId>', methods=['GET', 'POST'])
@login_required
def delete_poll(pollId):
    pass
    return render_template("current.html", title='Current Polls', users=users)

@bp.route('/response/<int:pollId>/delete/<int:userId>', methods=['GET', 'POST'])
@login_required
def delete_response(pollId,userId):
    pass
    return render_template("currentPollView.html", title='test', users=users)







@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template("profile.html", title='My Profile')



@bp.route('/test', methods=['GET', 'POST'])
def test():
    poll=getPollById(1)
    # myResponse={}
    responseParameter=[]
    for item in poll.Candidate:
        responseParameter.append((item.candidateId, item.candidateDescription))
    form=makeResponseForm(responseParameter)
    # print(responseParameter)
    # for item in form.responses:
    #     print("data:", item.id)
    #     print(item.description, item.label, item.data)  

    # if form.validate_on_submit():
    #     for item in form.responses:
    # #         print("dfkjskflsd",item.data)
    # return render_template("test.html", title='test', poll=poll, form=form)

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
