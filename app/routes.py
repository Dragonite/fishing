from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

user = {'nickname': 'Haolin', 'admin': 'true', 'id': 1}

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
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, user=user)

@app.route('/help')
def help():
    return render_template("help.html", title='Help', user=user)


    
@app.route('/currentStandingPolls')
def CurrentStandingPolls():
    return render_template("CurrentStandingPolls.html",
                           title='currentStandingPolls')




@app.route('/completedPolls')
def CompletedPolls():
    return render_template("CompletedPolls.html",
                           title='completedPolls')


@app.route('/createAPolls')
def CreateAPolls():
    return render_template("CreateAPolls",
                           title='createAPolls')

@app.route('/mProfile')
def MyProfile():
    return render_template("MyProfile.html",
                           title='myProfile')

@app.route('/logOut')
def LogOut():
    return render_template("LogOut.html",
                           title='logOut')

                 
