from flask import render_template, flash, redirect, url_for, Markup

from app import app
from app.forms import LoginForm, CreatePollForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import login_required


# Mimic Admin User
user = {'nickname': 'Haolin', 'admin': True, 'id': 1}

# Mimic Logged In User
# user = {'nickname': 'Leon', 'admin': False, 'id': 2}

# Mimic Default User
# user = {}


@app.route('/')
@app.route('/index')

def index():
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Haolin'},
            'body': 'I caught a herring!'
        },
        {
            'author': {'nickname': 'Luna'},
            'body': 'I caught a snapper!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(logInId=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        
        next_page = request.args.get('current')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('next_page'))
    return render_template('login.html', title='Sign In', form=form, user=User)



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
    return render_template('create.html', title='Create a Poll', form=form, user=user)


@app.route('/help')
def help():
    return render_template("help.html", title='Help', user=user)


@app.route('/current')
def current():
    return render_template("current.html", title='Current Polls', user=user)


@app.route('/completed')
def completed():
    return render_template("completed.html", title='Completed Polls', user=user)


@app.route('/create')
@login_required
def create():
    return render_template("create.html", title='Create A Poll', user=user)

@app.route('/users')
@login_required
def users():
    return render_template("users.html", title='Users', user=user)


@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", title='My Profile', user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))        




@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(logInId=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
