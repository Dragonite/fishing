from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app, Markup
from flask_login import current_user, login_required
# from flask_babel import _, get_locale
# from guess_language import guess_language
from app import db
import json

from app.models import User, Poll
from app.controllers import modifyPoll,archivePoll,createUser, createPoll, getCurrentPolls, getClosedPolls, getAllUsers, getPollById, getUserById, getAllPolls, archiveResponse, archiveUser
from app.main import bp

from app.pollForm import closePollForm,CreatePollForm,makeResponseForm,deleteUserForm,deletePollForm,deleteResponseForm
from app.registrationForm import RegistrationForm




@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    all_polls = getAllPolls()
    current_polls = len(getCurrentPolls())
    completed_polls = len(getClosedPolls())
    user_count = len(getAllUsers())
    my_polls = []
    if hasattr(current_user, 'userId'):
        for poll in all_polls:
            if poll.createdByUserId == current_user.userId:
                my_polls.append(poll)
    return render_template('index.html', title='Home', my_polls=len(my_polls), current_polls=current_polls, completed_polls=completed_polls, all_users=user_count)




@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreatePollForm()
    if form.validate_on_submit():
        validationPoll=Poll.query.filter_by(title=form.title.data).first()
        if validationPoll!= None:
            flash(Markup('<script>Notify("There is alreay a poll created with the same title.", null, null, "danger")</script>'))
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
                flash(Markup('<script>Notify("There is not enough choice to make this poll.", null, null, "danger")</script>'))
                return redirect(url_for('main.create'))
            else:
                if createPoll(poll)==True:
                    flash(Markup('<script>Notify("Poll has been created successfully!", null, null, "success")</script>'))
                    return redirect(url_for('main.current')+'/'+ str(poll.pollId))

                else:
                    flash(Markup('<script>Notify("something is wrong!", null, null, "danger")</script>'))
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
@login_required
def current_view(pollId):
    users = getAllUsers()
    poll=getPollById(pollId)
    if poll:
        responseParameter=[]
        for item in poll.Candidate:
            responseParameter.append((item.candidateId, item.candidateDescription))
        form=makeResponseForm(responseParameter)
        renderedtitle=poll.title
    else:
        flash(Markup('<script>Notify("Poll does not exist.", null, null, "danger")</script>'))
        return redirect(url_for('main.current'))
    if form.is_submitted():
        preferences=form.preferences
        pref={}
        for item in preferences:
            print(item.data)
        index=1;
        for item in preferences:
            pref[item.data]=pref.get(item.data, index)
            index +=1    
        if Poll.Response.query.filter_by(pollId=pollId).filter_by(userId=current_user.userId).first()!=None:
            flash(Markup('<script>Notify("You already have voted for this poll.", null, null, "danger")</script>'))
            return redirect(url_for('main.current'))
        else:
            if poll.addResponse(current_user.userId, pref):
                flash(Markup('<script>Notify("you have successfully voted for this poll.", null, null, "success")</script>'))
                return redirect(url_for('main.current'))
            else:
                flash(Markup('<script>Notify("Oops, Something went wrong!", null, null, "danger")</script>'))
    return render_template("poll-views/currentPollView.html", title=renderedtitle, poll=poll, form=form, users=users)

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
    return render_template("poll-views/completedPollView.html", title=renderedtitle, poll=poll, users=users)

@bp.route('/polls')
def polls_view():
    return redirect(url_for('main.current'))

@bp.route('/polls/<int:pollId>')
def specific_poll_view(pollId):
    poll=getPollById(pollId)
    if(poll.completedAt):
        return redirect(url_for('main.completed')+'/'+str(pollId))
    return redirect(url_for('main.current')+'/'+str(pollId))

@bp.route('/polls/<int:pollId>/archive', methods=['GET', 'POST'])
@login_required
def poll_archive(pollId):
    if current_user.is_authenticated:
        if current_user.isAdmin:
            users=getAllUsers()
            poll=getPollById(pollId)
            form= deleteResponseForm()
            if poll==None:
                flash(Markup('<script>Notify("Cannot find the poll.", null, null, "danger")</script>'))
            if form.is_submitted():
                if User.query.filter_by(userId=form.userId.data).first():
                    if archiveResponse(poll,int(form.userId.data)):
                        flash(Markup('<script>Notify("The response has been archived successfully", null, null, "success")</script>'))
                    else:
                        flash(Markup('<script>Notify("Could not archive the response", null, null, "danger")</script>'))
    return render_template("archive-components/responseArchive.html", title="Archive Responses: "+"Poll "+str(pollId), poll=poll, users=users, form=form)


@bp.route('/archive', methods=['GET', 'POST'])
@login_required
def archive_poll():
    if current_user.is_authenticated:
        if current_user.isAdmin:
            users=getAllUsers()
            polls=getAllPolls()
            form=deletePollForm()
            if form.is_submitted():
                poll=getPollById(form.pollId.data)
                if poll==None:
                    flash(Markup('<script>Notify("Cannot find the poll.", null, null, "danger")</script>'))
                else:
                    poll.close()
                    # modifyPoll(poll)
                    if archivePoll(poll):
                        flash(Markup('<script>Notify("The poll has been archived successfully", null, null, "success")</script>'))
                    else:
                        flash(Markup('<script>Notify("Could not archive the poll", null, null, "danger")</script>'))
        else:
            flash(Markup('<script>Notify("Only an admin user can view this page!", null, null, "danger")</script>'))
            return redirect(url_for('main.index'))
    return render_template("archive-components/pollArchive.html", title="Archive Poll", polls=polls, users=users, form=form)




@bp.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    
    if current_user.isAdmin:
        users=getAllUsers()
        return render_template("users.html", title='Users', users=users)
    else:
        flash(Markup('<script>Notify("Only an admin user can view this page!", null, null, "danger")</script>'))
        return redirect(url_for('main.index'))

@bp.route('/users/archive', methods=['GET', 'POST'])
@login_required
def archive_users():
    if current_user.is_authenticated:
        if current_user.isAdmin:
            users=getAllUsers()
            form=deleteUserForm()
            if form.is_submitted():
                user=getUserById(form.userId.data)
                if user==None:
                    flash(Markup('<script>Notify("Cannot find the user.", null, null, "danger")</script>'))
                else:
                    if archiveUser(user):
                        flash(Markup('<script>Notify("The user  has been archived successfully", null, null, "success")</script>'))
                    else:
                        flash(Markup('<script>Notify("Could not archive the user", null, null, "danger")</script>'))
        else:
            flash(Markup('<script>Notify("Only an admin user can view this page!", null, null, "danger")</script>'))
            return redirect(url_for('main.index'))
    return render_template("archive-components/userArchive.html", title='Users', users=users, form=form)



# @bp.route('/users/delete/<int:userId>', methods=['GET', 'POST'])
# @login_required
# def delete_user(userId):
#     pass
#     return render_template("users.html", title='Users', users=users)

# @bp.route('/polls/delete/<int:pollId>', methods=['GET', 'POST'])
# @login_required
# def delete_poll(pollId):
#     pass
#     return render_template("current.html", title='Current Polls', users=users)

# @bp.route('/response/<int:pollId>/delete/<int:userId>', methods=['GET', 'POST'])
# @login_required
# def delete_response(pollId,userId):
#     pass
#     return render_template("currentPollView.html", title='test', users=users)







@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    all_polls = getAllPolls()
    polls = []
    form=closePollForm()
    for poll in all_polls:
        if poll.createdByUserId == current_user.userId:
            polls.append(poll)
    if form.validate_on_submit():
        myPoll = getPollById(form.pollId.data)
        myPoll.close()
        if modifyPoll(myPoll):
            flash(Markup('<script>Notify("Poll has been closed successfully!", null, null, "success")</script>'))

    return render_template("profile.html", title='My Profile', polls=polls, form=form)



# @bp.route('/test', methods=['GET', 'POST'])
# def test():
#     poll=getPollById(1)
#     # myResponse={}
#     responseParameter=[]
#     for item in poll.Candidate:
#         responseParameter.append((item.candidateId, item.candidateDescription))
#     form=makeResponseForm(responseParameter)
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
        if createUser(user,form.password.data)==True:
            flash(Markup('<script>Notify("Congratulations, you are now a registered user!", null, null, "success")</script>'))
            return redirect(url_for('auth.login'))
        else:
            flash(Markup('<script>Notify("Could not create account, please enter username, password, email and first name!", null, null, "danger")</script>'))
            return redirect(url_for('main.register'))
    return render_template('register.html', title='Register', form=form)


@bp.route('/users/create', methods=['GET', 'POST'])
def create_user():
    form = RegistrationForm()
    if current_user.is_authenticated:
        if current_user.isAdmin:
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
                    flash(Markup('<script>Notify("you have created a new user!", null, null, "success")</script>'))
                    return redirect(url_for('main.users'))
                else:
                    flash(Markup('<script>Notify("Could not create account, please enter username, password, email and first name!", null, null, "danger")</script>'))

    else:
            flash(Markup('<script>Notify("Only an admin user can view this page!", null, null, "danger")</script>'))
            return redirect(url_for('main.index'))
    return render_template('register.html', title='Register', form=form)
