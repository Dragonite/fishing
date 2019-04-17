from flask import render_template, flash, redirect, url_for, Markup
from app import app
from app.forms import LoginForm

# Mimic Admin User
user = {'nickname': 'Haolin', 'admin': True, 'id': 1}

# Mimic Logged In User
#user = {'nickname': 'Leon', 'admin': False, 'id': 2}

# Mimic Default User
# user={}

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
    form = LoginForm()
    if form.validate_on_submit():
        message=Markup('<script>Notify("Login requested for user {}, Remember me = {}", null, null, "danger")</script>'.format(form.username.data, form.remember_me.data))
        flash(message)
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, user=user)

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
def create():
    return render_template("create.html", title='Create A Poll', user=user)

@app.route('/users')
def users():
    return render_template("users.html", title='Users', user=user)

@app.route('/profile')
def profile():
    return render_template("profile.html", title='My Profile', user=user)

                 

import sqlite3


'''@app.route('/dbtest')
def dbtest():
    conn = sqlite3.connect('test.db')
    msg= "Opened database successfully"
    return render_template("dbtest.html", msg=msg)
    conn.close()'''